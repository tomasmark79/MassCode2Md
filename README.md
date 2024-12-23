# MassCode2Md

is a lightweight tool designed to convert code snippets stored in JSON format into organized Markdown files. The tool reads a JSON file containing code snippets and automatically arranges them into directories based on the provided structure in the JSON file.

Program have no robust controls and checks, so be careful for pass the right arguments. Output folder must exist before generating md files.

```bash
Usage: ./MassCode2MdStandalone <db.json> <output_folder>
```

example
```bash
./MassCode2MdStandalone db.json ./out
```

Set the paths and run. That's all.

To understand the project structure, jump to 👇

---

# MarkWare VCMake Template 🎁
v0.0.5

### Brief Description 📑

This solution represents a **complete workflow** for **modern** C/C++ software development. It integrates tools such as **VSCode**, **Conan**, **CMake**, **CPM.cmake**, **ModernCppStarter**, **TemplateRenamer**, **Formatters**, and more into a single functional unit. It allows you to create a **Standalone Application** and a **library** *immediately*.

### My Goal 🎯

To create a project template for myself that is flexible, works out of the box, and saves me a lot of time.

### The Result of my efforts 🧑🏻‍💻

Is a modular and intelligently designed project structure that gives me enormous flexibility and decision-making power at every point on how the project will be configured. For others, it may take a while to get used to the project, but in return, you will be pleasantly surprised at how simple it actually is.

### Deep Dive 🤿

##### VSCode

is an indispensable editor, ranking first due to its flexibility and configurability.  
  
##### VSCode Tasks

are predefined tasks in Visual Studio Code that automate common development workflows, such as building, cleaning, and running your project. These tasks are defined in the `tasks.json` file and can be customized to fit your specific needs.

##### Conan 2

is a powerful dependency manager for C/C++ projects. It simplifies the process of adding and managing libraries that your project may need. With Conan 2, you can easily specify the dependencies in a `conanfile.txt` or `conanfile.py`, and it will handle the downloading, building, and integrating of these libraries into your project. This ensures that you always have the correct versions of the libraries and that they are configured properly for your development environment. Conan 2 also supports package creation, allowing you to create and share your own libraries with others.

##### CMake

as a modern configurator with object-oriented elements, provides enormous flexibility.

##### CPM.cmake

add simplified support for fetching packages from GitHub, ensuring an easier way to obtain such packages.

##### CPM.Licenses

also helps in managing and writing license files for the dependencies used in the project.

##### ModernCppStarter

is a project structure proven over many years and projects for developing programs and libraries. The essence of this structure is also embedded in this project.

##### TemplateRenamer

is a script that allows you to rename the template project to your desired names for both the library and the standalone application. This ensures that the project is uniquely identified and tailored to your specific needs.
  
##### Formatters

are simple scripts that quickly reformat C/C++ and CMake files.

### List of dependencies 🔃

 - Linux 🐧 or Mac
 - VSCode - https://code.visualstudio.com (mandatory)
 - CMake - https://cmake.org/download/ (mandatory)
 - Python3 - https://www.python.org/downloads/ (mandatory)
 - Conan2 Configurator - https://docs.conan.io/2/installation.html (mandatory)
 - Compilers - https://gcc.gnu.org, https://clang.llvm.org, ... (mandatory)
 - Cmake-formatter - https://cmake-format.readthedocs.io/en/latest/ (optional)
 - Clang-formatter - https://clang.llvm.org/docs/ClangFormat.html (optional)
 - Cross-compiler with a toolchain and a sysroot - https://crosstool-ng.github.io (optional)

### Quick Start 💣


https://github.com/user-attachments/assets/60b51d6a-1724-4b05-9cc8-94683e2f2131


```bash
# clone 
git clone https://github.com/tomasmark79/MarkWareVCMake ./NameOfMyAwesomeApp
cd NameOfMyAwesomeApp/
code .
```

### Integrated VSCode Tasks and Key Associations

#### F5

- Debug

#### F7

- Build Native Debug  
notice: (no menu appearing, direct building only)

#### **Shift+F7**

Displays a menu with items such as:

- Build
- Rebuild
- Configure
- Conan
- Clean
- Install
- Licenses

The menu shows 3 variants of items:

- for both targets
- for Standalone
- for Library

### Project filesystem structure description

```txt
tree -a --prune -I '.git|Build|Hidden'
.
├── .clang-format - configuration file for clang-format, a tool to format C/C++/Objective-C/...
├── cmake - directory containing CMake-related scripts and modules
│   ├── CPM.cmake - is a cross-platform CMake script that adds dependency management capabilities to CMake
│   ├── Modules - directory for custom CMake modules
│   │   └── FindX11.cmake - custom CMake module to find X11 libraries
│   └── tools.cmake - CMake script for additional tools and utilities
├── CMakeController.sh - shell script to control CMake build process
├── .cmake-format - configuration file for cmake-format, a tool to format CMake scripts
├── CMakeLists.txt - main CMake build script for library
├── CMakeUserPresets.json - JSON file containing user presets for CMake
├── conanfile.txt - Conan package manager configuration file
├── .gitattributes - Git configuration file for defining attributes per path
├── .gitignore - Git configuration file to specify untracked files to ignore
├── include - directory containing header files
│   └── VCMLib - directory for VCMLib library headers
│       └── VCMLib.hpp - header file for VCMLib library
├── LICENSE - license file for the project
├── .python-version - file specifying the Python version for the project
├── README.md - markdown file containing the project documentation
├── Source - directory containing source files
│   └── VCMLib.cpp - source file for VCMLib library
├── Standalone - directory for standalone application
│   ├── CMakeLists.txt - CMake build script for standalone application
│   ├── LICENSE - license file for standalone application
│   └── Source - directory containing source files for standalone application
│       └── Main.cpp - main source file for standalone application
├── TemplateRenamer.sh - shell script to rename names for standalone and library
└── .vscode - directory containing Visual Studio Code configuration files
├── c_cpp_properties.json - VSCode configuration file for C/C++ properties
├── keybindings.json - VSCode configuration file for custom keybindings
├── launch.json - VSCode configuration file for debugging settings
├── settings.json - VSCode configuration file for workspace settings
└── tasks.json - VSCode configuration file for defining tasks
```

##### Useful to Know

`└── TemplateRenamer.sh`

This shell script is a very powerful renamer for the entire project. After cloning the repository into your folder, you can use this script to create your own names for both the library and the application. The names must not be the same.

```bash
Usage: ./TemplateRenamer.sh <old_lib_name> <new_lib_name> <old_standalone_name> <new_standalone_name>
```
  
### ToDo

I still want to add:
- 🚧 add installation CMake configuration
- prepare list of commands for CLI-only workflow
- port to MS Windows family OS
- include some other features useful for developers

### My Code Codex
               
I use capital letters at the beginning of words for naming all new folders and files.  
One exception: No capital letter in the "include" folder is intentional!

### I drew inspiration from the following projects

- [ModernCppStarter](https://github.com/TheLartians/ModernCppStarter)
- [PackageProject.cmake](https://github.com/TheLartians/PackageProject.cmake)
- [CPM.cmake](https://github.com/cpm-cmake/CPM.cmake)
- [CPMLicenses.cmake](https://github.com/cpm-cmake/CPMLicenses.cmake.git)
  
Thanks to Sleepy Monax for Mac OS feedback.

---

### About Me 🧑🏻‍💻

"The result of a lot of hours of incredible work. Time seemed to stand still. The outcome is a template that takes C++ development to a whole new level. 
    
"Buy me a coffee ☕🍵 or spare some time. 🙂"

```
paypal.me/TomasMark
Bitcoin: 3JMZR6SQo65kLAxxxXKrVE7nBKrixbPgSZ
Ethereum: 0x7a6C564004EdecFf8DD9EAd8bD4Bbc5D2720BeE7
```

MIT License

Copyright (c) 2024 Tomáš Mark
