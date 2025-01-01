cmake_minimum_required(VERSION 3.14 FATAL_ERROR)

cmake_policy(SET CMP0091 NEW)

# ==============================================================================
# Static or shared compiling
# ==============================================================================
option(BUILD_SHARED_LIBS "Build using shared libraries" OFF)

# Linting C/C++ code
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# ==============================================================================
# Project attributes
# ==============================================================================
set(STANDALONE_NAME MassCode2MdStandalone)
string(TOLOWER "${STANDALONE_NAME}" STANDALONE_NAME_LOWER)
set(STANDALONE_NAMESPACE dsdotname)
project(
    ${STANDALONE_NAME}
    LANGUAGES C CXX ASM
    DESCRIPTION "template Copyright (c) 2024 TomasMark [at] digitalspace.name"
    HOMEPAGE_URL "https://github.com/tomasmark79")

# ---- Include guards ----
if(PROJECT_SOURCE_DIR STREQUAL PROJECT_BINARY_DIR)
    message(FATAL_ERROR "In-source builds not allowed.
            Please make a new directory (called a Build directory) and run CMake from there.")
endif()

# ==============================================================================
# System / Conan dependencies
# ==============================================================================
list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/cmake/Modules")

# ==============================================================================
# CPM.cmake dependencies - take care conflicts
# ==============================================================================
include(../cmake/tools.cmake)
include(../cmake/CPM.cmake)
CPMAddPackage(NAME MassCode2Md SOURCE_DIR ${CMAKE_CURRENT_LIST_DIR}/..)

# ==============================================================================
# Source and header files Glob not recommended, but the simplest way for this template
# ==============================================================================
file(
    GLOB_RECURSE
    headers
    CONFIGURE_DEPENDS
    ${CMAKE_CURRENT_SOURCE_DIR}/include/*.h
    ${CMAKE_CURRENT_SOURCE_DIR}/include/*.hpp
    ${CMAKE_CURRENT_SOURCE_DIR}/include/*.hh
    ${CMAKE_CURRENT_SOURCE_DIR}/include/*.hxx)
file(
    GLOB_RECURSE
    sources
    CONFIGURE_DEPENDS
    ${CMAKE_CURRENT_SOURCE_DIR}/Source/*.c
    ${CMAKE_CURRENT_SOURCE_DIR}/Source/*.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/Source/*.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/Source/*.cxx)

# ==============================================================================
# Create target
# ==============================================================================
add_executable(${STANDALONE_NAME} ${sources})

# ==============================================================================
# Set compile properties
# ==============================================================================
set_target_properties(${STANDALONE_NAME} PROPERTIES OUTPUT_NAME "${STANDALONE_NAME}")

# ==============================================================================
# Set linking
# ==============================================================================
target_link_libraries(${STANDALONE_NAME} PRIVATE dsdotname::MassCode2Md)

# ==============================================================================
# Set installation directory
# ==============================================================================
install(TARGETS ${STANDALONE_NAME} RUNTIME DESTINATION bin)
