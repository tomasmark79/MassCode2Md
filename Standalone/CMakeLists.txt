cmake_minimum_required(VERSION 3.20 FATAL_ERROR)

# (c) Tomáš Mark 2024

# ---- Project Standalone namespace::name  ----
set(PROJECT_STANDALONE_NAMESPACE dsdotname)
set(PROJECT_STANDALONE_NAME MassCode2MdStandalone) # for change use
                                                   # ./TemplateRenamer.sh

# ---- Generate Static/Shared targets (used by Conan as well) ----
option(BUILD_SHARED_LIBS "Build using shared libraries" OFF)

# ---- Project ----
project(${PROJECT_STANDALONE_NAME} LANGUAGES C CXX ASM)

# ---- Include guards ----
if(PROJECT_SOURCE_DIR STREQUAL PROJECT_BINARY_DIR)
    message(
        FATAL_ERROR
            "In-source builds not allowed. Please make a new directory (called a build directory) and run CMake from there."
    )
endif()

# ---- CPMs -----
include(../cmake/CPM.cmake)
include(../cmake/tools.cmake)

# ---- CMake Modules ----
set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH}
                      "${PROJECT_SOURCE_DIR}../cmake/Modules")

cpmaddpackage(NAME MassCode2Md SOURCE_DIR ${CMAKE_CURRENT_LIST_DIR}/..)

# Glob not recommended, but the simplest way for this template
file(GLOB sources CONFIGURE_DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/Source/*.cpp
     ${CMAKE_CURRENT_SOURCE_DIR}/Source/*.c)

# ---- Create standalone executable ----
add_executable(${PROJECT_STANDALONE_NAME} ${sources})

# ---- Standalone options ----
set_target_properties(${PROJECT_STANDALONE_NAME}
                      PROPERTIES OUTPUT_NAME "${PROJECT_STANDALONE_NAME}")

target_link_libraries(${PROJECT_STANDALONE_NAME} PRIVATE dsdotname::MassCode2Md)

# ---- Install ----
