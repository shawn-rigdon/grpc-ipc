cmake_minimum_required (VERSION 2.8.11)
project(shm_ipc)

if (NOT DEFINED GENERATED_DIR)
    set(GENERATED_DIR "${CMAKE_BINARY_DIR}/generated")
endif()
if (NOT DEFINED CMAKE_RUNTIME_OUTPUT_DIRECTORY)
    set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/bin)
endif()
if (NOT DEFINED CMAKE_LIBRARY_OUTPUT_DIRECTORY)
    set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/lib)
endif()

option(BUILD_SHARED_LIBS "build shared libraries" ON)

#add_subdirectory("${CMAKE_SOURCE_DIR}/dependencies/grpc")
set(GRPC_INSTALL_DIR "${CMAKE_CURRENT_LIST_DIR}/dependencies/grpc")
add_subdirectory(${GRPC_INSTALL_DIR})

#set(GRPC_INSTALL_DIR "${CMAKE_SOURCE_DIR}/lib/grpc")
#set(GRPC_INCLUDE_DIR "${GRPC_INSTALL_DIR}/include")
#set(GRPC_LIB_DIR "${GRPC_INSTALL_DIR}/lib")

set(GRPC_INCLUDE_DIR ${GRPC_INSTALL_DIR}/${gRPC_INSTALL_INCLUDEDIR})
set(PROTO_SRC "${GRPC_INSTALL_DIR}/third_party/protobuf/src")

add_subdirectory(server)
add_subdirectory(client)