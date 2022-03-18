
#include <grpcpp/grpcpp.h>

#include <atomic>
#include <csignal>
#include <iostream>
#include <memory>
#include <mutex> // For std::unique_lock
#include <shared_mutex>
#include <sstream>
#include <string>
#include <unordered_map>

#include <fcntl.h> /* For O_* constants */
#include <sys/mman.h>
#include <sys/stat.h> /* For mode constants */
#include <sys/types.h>
#include <unistd.h>

#include <batlshm.grpc.pb.h>
//#include "spdlog/spdlog.h"

#include "shm_manager.h"
#include "topic_manager.h"

using namespace std;
using grpc::Server;
using grpc::ServerBuilder;
using grpc::ServerContext;
using grpc::Status;

class BatlShmServiceImpl final : public BatlShm::Service {
private:
  mutex mMutex;

public:
  Status CreateBuffer(ServerContext *context,
                      const CreateBufferRequest *request,
                      CreateBufferReply *reply) override {
    reply->set_result(-1);

    // create buffer name
    static std::atomic<unsigned int> count(0);
    string name = "/batl_" + to_string(count++);

    shared_ptr<ShmBuffer> buffer = make_shared<ShmBuffer>(name);
    if (!buffer->allocate(request->size()))
      return Status::CANCELLED;

    ShmManager::getInstance()->add(buffer);
    reply->set_name(name);
    reply->set_result(0);
    return Status::OK;
  }

  Status GetBuffer(ServerContext *context, const GetBufferRequest *request,
                   GetBufferReply *reply) override {
    reply->set_result(-1);
    shared_ptr<ShmBuffer> buffer =
        ShmManager::getInstance()->getBuffer(request->name());
    if (buffer) {
      reply->set_size((uint32_t)buffer->getSize());
      reply->set_result(0);
    }

    return Status::OK;
  }

  Status ReleaseBuffer(ServerContext *context,
                       const ReleaseBufferRequest *request,
                       StandardReply *reply) override {
    string name = request->name();
    ShmManager::getInstance()->release(name);
    reply->set_result(0);
    return Status::OK;
  }

  Status RegisterTopic(ServerContext *context,
                       const RegisterTopicRequest *request,
                       StandardReply *reply) override {
    reply->set_result(0);
    string name = request->name();
    if (!TopicManager::getInstance()->addTopic(name))
      reply->set_result(-1); // topic already exists

    return Status::OK;
  }

  Status Publish(ServerContext *context, const PublishRequest *request,
                 StandardReply *reply) override {
    reply->set_result(-1);
    string buffer_name = request->buffer_name();
    shared_ptr<ShmBuffer> shm_buf =
        ShmManager::getInstance()->getBuffer(buffer_name);
    if (!shm_buf)
      return Status::OK;

    unsigned int sub_count =
        TopicManager::getInstance()->getSubscriberCount(request->topic_name());
    shm_buf->setRefCount(sub_count);
    TopicQueueItem msg(buffer_name, request->metadata(), request->timestamp());
    if (TopicManager::getInstance()->publish(request->topic_name(), msg)) {
      reply->set_result(0);
      // TODO: This should probably be handled by a client object. We don't want
      // this function
      //      to assume a buffer needs to get released.
    } else
      ShmManager::getInstance()->release(buffer_name, sub_count);

    return Status::OK;
  }

  Status GetSubscriberCount(ServerContext *context,
                            const SubscriberCountRequest *request,
                            SubscriberCountReply *reply) override {
    unsigned int sub_count =
        TopicManager::getInstance()->getSubscriberCount(request->topic_name());
    reply->set_num_subs(sub_count);
    reply->set_result(0);
    return Status::OK;
  }

  //    //TODO: NEXT - figure out how to return repeated
  //    Status GetTopics(ServerContext* context, Empty* e, TopicList* tl)
  //    override {
  //    }

  Status Subscribe(ServerContext *context, const SubscribeRequest *request,
                   StandardReply *reply) override {
    reply->set_result(0);
    std::cout << "Subscribe request from: " << request->subscriber_name()
              << std::endl;
    std::vector<string> dep;
    dep.reserve(request->dependencies_size());
    std::cout << "dependencies size: " << request->dependencies_size()
              << std::endl;
    for (int i = 0; i < request->dependencies_size(); ++i)
      dep.emplace_back(request->dependencies(i));

    if (!TopicManager::getInstance()->subscribe(request->topic_name(),
                                                request->subscriber_name(), dep,
                                                request->maxqueuesize()))
      reply->set_result(-1);

    return Status::OK;
  }

  Status Pull(ServerContext *context, const PullRequest *request,
              PullReply *reply) override {
    string topic = request->topic_name();
    string subscriber = request->subscriber_name();
    int timeout = request->timeout();
    TopicQueueItem item;
    reply->set_result(-1);
    // Clear processed queue items for this set of subscribers.
    // This is done here to support client cancellation.
    TopicManager::getInstance()->clearOldPosts(topic, subscriber);
    bool gotItem =
        TopicManager::getInstance()->pull(topic, subscriber, item, timeout);
    if (!gotItem)
      return Status::OK;

    unique_lock<mutex> lock(mMutex);
    if (context->IsCancelled()) {
      TopicManager::getInstance()->cancelPull(topic, subscriber);
      return Status::CANCELLED;
    }

    if (!item.buffer_name.empty()) {
      reply->set_result(0);
      reply->set_buffer_name(item.buffer_name);
      reply->set_metadata(item.metadata);
      reply->set_timestamp(item.timestamp);
    }

    return Status::OK;
  }
};

void RunServer() {
  std::string server_address("0.0.0.0:50051");
  BatlShmServiceImpl service;

  ServerBuilder builder;
  // Listen on the given address without any authentication mechanism.
  builder.AddListeningPort(server_address, grpc::InsecureServerCredentials());
  // Register "service" as the instance through which we'll communicate with
  // clients. In this case it corresponds to an *synchronous* service.
  builder.RegisterService(&service);
  // Finally assemble the server.
  std::unique_ptr<Server> server(builder.BuildAndStart());

  // Wait for the server to shutdown. Note that some other thread must be
  // responsible for shutting down the server for this call to ever return.
  server->Wait();
}

void SignalHandler(int signum) {
  ShmManager::getInstance()->releaseAll();
  exit(signum);
}

int main(int argc, char **argv) {
  std::signal(SIGINT, SignalHandler); // release memory if server is terminated
  // spdlog::set_level(spdlog::level::debug);
  RunServer();
  return 0;
}
