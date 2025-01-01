name: Install

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

env:
  CPM_SOURCE_CACHE: ${{ github.workspace }}/cpm_modules

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4
      - uses: actions/cache@v3
        with:
          path: "**/cpm_modules"
          key: ${{ github.workflow }}-cpm-modules-${{ hashFiles('**/CMakeLists.txt', '**/*.cmake') }}
     
      - name: configureLibrary
        run: cmake -S . -B Build/Library/Debug -DCMAKE_BUILD_TYPE=Debug
      - name: makeLibrary
        run: cmake --build Build/Library/Debug --target all
      - name: installLibrary
        run: cmake --install Build/Library/Debug --prefix Build/Library/Debug/Install
      
      - name: configureStandalone
        run: cmake -S ./Standalone -B Build/Standalone/Debug -DCMAKE_BUILD_TYPE=Debug
      - name: makeStandalone
        run: cmake --build Build/Standalone/Debug --target all
      - name: installStandalone
        run: cmake --install Build/Standalone/Debug --prefix Build/Standalone/Debug/Install
