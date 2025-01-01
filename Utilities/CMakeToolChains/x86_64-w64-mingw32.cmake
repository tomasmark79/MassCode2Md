# (c) Tomáš Mark 2024

set(CMAKE_SYSTEM_NAME Windows)
set(CMAKE_SYSTEM_PROCESSOR x86_64)
set(user_dir "/home/tomas") # edit me
set(triple "x86_64-w64-mingw32")

set(CMAKE_SYSROOT ${user_dir}/x-tools/${triple}/${triple}/sysroot)

set(CMAKE_C_COMPILER ${user_dir}/x-tools/${triple}/bin/${triple}-gcc)
set(CMAKE_CXX_COMPILER ${user_dir}/x-tools/${triple}/bin/${triple}-g++)
set(CMAKE_ASM_COMPILER ${user_dir}/x-tools/${triple}/bin/${triple}-as)
set(CMAKE_LINKER ${user_dir}/x-tools/${triple}/bin/${triple}-ld)
set(CMAKE_AR ${user_dir}/x-tools/${triple}/bin/${triple}-ar)
set(CMAKE_RANLIB ${user_dir}/x-tools/${triple}/bin/${triple}-ranlib)
set(CMAKE_STRIP ${user_dir}/x-tools/${triple}/bin/${triple}-strip)
set(CMAKE_LIBTOOL ${user_dir}/x-tools/${triple}/bin/${triple}-libtool)

# where is the CMAKE_FIND_ROOT_PATH target environment located
set(CMAKE_FIND_ROOT_PATH ${CMAKE_SYSROOT})

# adjust the default behavior of the FIND_XXX() commands: search programs in the host environment
set(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)

# search headers and libraries in the target environment
set(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
set(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)

# Set the path for pkg-config
set(ENV{PKG_CONFIG_PATH} "${CMAKE_SYSROOT}/usr/lib/pkgconfig:${CMAKE_SYSROOT}/usr/share/pkgconfig")
