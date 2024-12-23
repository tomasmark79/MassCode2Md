# (c) Tomáš Mark 2024

# Set system name and processor
set(CMAKE_SYSTEM_NAME Linux)
set(CMAKE_SYSTEM_PROCESSOR aarch64)
set(CROSS_HOST "arm-linux-gnu") # This is the host system

# Define sysroot
set(CMAKE_SYSROOT
    /home/tomas/x-tools/aarch64-rpi4-linux-gnu/aarch64-rpi4-linux-gnu/sysroot)

# Specify cross-compilers
set(CMAKE_C_COMPILER
    /home/tomas/x-tools/aarch64-rpi4-linux-gnu/bin/aarch64-rpi4-linux-gnu-gcc)
set(CMAKE_CXX_COMPILER
    /home/tomas/x-tools/aarch64-rpi4-linux-gnu/bin/aarch64-rpi4-linux-gnu-g++)
set(CMAKE_ASM_COMPILER
    /home/tomas/x-tools/aarch64-rpi4-linux-gnu/bin/aarch64-rpi4-linux-gnu-as)
set(CMAKE_LINKER
    /home/tomas/x-tools/aarch64-rpi4-linux-gnu/bin/aarch64-rpi4-linux-gnu-ld)
set(CMAKE_AR
    /home/tomas/x-tools/aarch64-rpi4-linux-gnu/bin/aarch64-rpi4-linux-gnu-ar)
set(CMAKE_RANLIB
    /home/tomas/x-tools/aarch64-rpi4-linux-gnu/bin/aarch64-rpi4-linux-gnu-ranlib
)
set(CMAKE_STRIP
    /home/tomas/x-tools/aarch64-rpi4-linux-gnu/bin/aarch64-rpi4-linux-gnu-strip)
set(CMAKE_LIBTOOL
    /home/tomas/x-tools/aarch64-rpi4-linux-gnu/bin/aarch64-rpi4-linux-gnu-libtool
)

# where is the CMAKE_FIND_ROOT_PATH target environment located
set(CMAKE_FIND_ROOT_PATH ${CMAKE_SYSROOT})

# adjust the default behavior of the FIND_XXX() commands: search programs in the
# host environment
set(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)

# search headers and libraries in the target environment
set(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
set(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)

# Set the path for pkg-config
set(ENV{PKG_CONFIG_PATH}
    "${CMAKE_SYSROOT}/usr/lib/pkgconfig:${CMAKE_SYSROOT}/usr/share/pkgconfig")
