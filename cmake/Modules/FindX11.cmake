find_package(PkgConfig)
pkg_check_modules(X11 REQUIRED x11)

include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(X11 DEFAULT_MSG X11_FOUND)
