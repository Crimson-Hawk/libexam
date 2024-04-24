cmake_minimum_required(VERSION 2.8)

project(libexam CXX)

set(SOURCE_FILES libexam.cpp SHA256.cpp SHA256.h)
set(CMAKE_CXX_FLAGS "${compiler_common_flags} ${CMAKE_CXX_FLAGS} -std=c++17")
add_library(${PROJECT_NAME} ${SOURCE_FILES})

target_include_directories(${PROJECT_NAME} PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})