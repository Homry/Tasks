cmake_minimum_required(VERSION 3.17)
project(rotateTriangle)

set(CMAKE_CXX_STANDARD 20)
set(OpenGlLinkers -lglut -lGLU -lGL)
add_executable(rotateTriangle main.cpp source/quaternion.h source/vector3D.h source/matrix.h source/RigidBody.h source/Screen.h)
target_link_libraries(rotateTriangle ${OpenGlLinkers})