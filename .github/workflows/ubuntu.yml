name: Ubuntu

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

env:
  CPM_SOURCE_CACHE: ${{ github.workspace }}/.cpm_modules
  BUILD_TYPE: Release

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: create CPM cache
        id: cache-cpm
        uses: actions/cache@v3
        with:
          path: ${{env.CPM_SOURCE_CACHE}}
          key: ${{ runner.os }}-cpm-${{ hashFiles('**/cmake/CPM.cmake') }}

      - name: install conan to system
        run: |
          sudo apt-get update
          sudo apt-get install -y python3-pip
          pip3 install conan

      - name: create Conan cache
        id: cache-conan
        uses: actions/cache@v3
        with:
          path: /home/runner/.conan2
          key: ${{ runner.os }}-conan-${{ hashFiles('**/conanfile.py') }}

      - if: ${{ steps.cache-conan.outputs.cache-hit != 'true' }}
        name: Conan profile detect --force
        run: conan profile detect --force
      
      - name: Conan profile show
        run: conan profile show

      - name: install Conan dependencies
        run: conan install . -s build_type=${{env.BUILD_TYPE}} -of=${{github.workspace}}/build -pr default -b=missing
      
      - name: CMake configure Library
        run: cmake -B ${{github.workspace}}/build -DCMAKE_TOOLCHAIN_FILE=conan_toolchain.cmake -DCMAKE_BUILD_TYPE=${{env.BUILD_TYPE}}
      
      - name: CMake build Library
        run: cmake --build ${{github.workspace}}/build --config ${{env.BUILD_TYPE}}
      
      - name: CMake configure Standalone
        run: cmake -S ./Standalone -B ${{github.workspace}}/build/Standalone -DCMAKE_TOOLCHAIN_FILE=../conan_toolchain.cmake -DCMAKE_BUILD_TYPE=${{env.BUILD_TYPE}}
        
      - name: CMake build Standalone
        run: cmake --build ${{github.workspace}}/build/Standalone --config ${{env.BUILD_TYPE}}
