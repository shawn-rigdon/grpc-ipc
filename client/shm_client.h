#pragma once

#include <string>
#include <grpcpp/grpcpp.h>

#include "batlshm.grpc.pb.h"

using grpc::Channel;
using std::string;

using namespace std;

enum BatlShmErrorCodes {
    OK = 0,
    FAILED = -1,
    TIMEOUT = -2
};

class BatlShmClient {
private:
    unique_ptr<BatlShm::Stub> mStub;

public:
    BatlShmClient(shared_ptr<Channel> channel);

    int32_t CreateBuffer(string& name, int32_t size);
    int32_t GetBuffer(const string& name, int32_t& size);
    int32_t ReleaseBuffer(const string& name);
    int32_t RegisterTopic(const string& name);
    int32_t Publish(const string& topic_name, const string& buffer_name, uint64_t timestamp);
    int32_t GenerateID(uint32_t& id);
    int32_t Subscribe(const string& topic_name, const uint32_t id);
    int32_t Pull(const string& topic_name, const uint32_t id, 
            string& buffer_name, uint64_t timestamp);
};

void* MapBuffer(const string& handle, size_t size);
void UnmapBuffer(void* memory, size_t size);