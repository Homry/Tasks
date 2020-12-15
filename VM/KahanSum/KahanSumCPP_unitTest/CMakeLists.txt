cmake_minimum_required(VERSION 3.15)
project(unit)

set(CMAKE_CXX_STANDARD 17)

add_executable(unit main.cpp unitTest.h test.h  ../KahanSumCPP/KahanSum.h)


