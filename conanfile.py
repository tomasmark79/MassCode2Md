from conan import ConanFile
from conan.tools.cmake import cmake_layout

class CompressorRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps"


    def requirements(self):
        self.requires("zlib/1.2.11")
        self.requires("fmt/11.0.2")
        self.requires("nlohmann_json/3.11.2")
        #self.requires("libcurl/8.10.1")
    
    #def build_requirements(self):
        #self.tool_requires("cmake/3.22.6")

    #def layout(self):
        #cmake_layout(self)