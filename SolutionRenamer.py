import os
import sys
import shutil
import codecs # For reading and writing files with utf-8 specific encoding (required for Windows)

def rename_project(old_lib_name, new_lib_name, old_standalone_name, new_standalone_name):
    # Convert to lowercase and uppercase
    old_lib_name_lower = old_lib_name.lower()
    new_lib_name_lower = new_lib_name.lower()
    old_lib_name_upper = old_lib_name.upper()
    new_lib_name_upper = new_lib_name.upper()

    # new_lib_name and new_standalone_name must not be the same
    if new_lib_name == new_standalone_name:
        print("Error: new_lib_name and new_standalone_name must be different")
        sys.exit(1)

    # List of files where the project names should be changed
    files = [
        ".vscode/launch.json",
        "LICENSE",
        "CMakeLists.txt",
        f"include/{old_lib_name}/{old_lib_name}.hpp",
        f"Source/{old_lib_name}.cpp",
        "Standalone/CMakeLists.txt",
        "Standalone/Source/Main.cpp",
        # Add more files as needed
    ]

    # Replace the old library name with the new one in each file
    for file in files:
        if os.path.isfile(file):
            with codecs.open(file, 'r', encoding='utf-8') as f:
                content = f.read()
            content = content.replace(old_lib_name, new_lib_name)
            content = content.replace(old_standalone_name, new_standalone_name)
            content = content.replace(old_lib_name_lower, new_lib_name_lower)
            content = content.replace(old_lib_name_upper, new_lib_name_upper)
            with codecs.open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Renamed project names in file: {file}")
        else:
            print(f"File {file} does not exist!")

    # Rename files
    if os.path.isfile(f"Source/{old_lib_name}.cpp"):
        os.rename(f"Source/{old_lib_name}.cpp", f"Source/{new_lib_name}.cpp")
        print(f"Renamed file: Source/{old_lib_name}.cpp to Source/{new_lib_name}.cpp")

    if os.path.isfile(f"include/{old_lib_name}/{old_lib_name}.hpp"):
        os.rename(f"include/{old_lib_name}/{old_lib_name}.hpp", f"include/{old_lib_name}/{new_lib_name}.hpp")
        print(f"Renamed file: include/{old_lib_name}/{old_lib_name}.hpp to include/{old_lib_name}/{new_lib_name}.hpp")

    # Rename directories
    if os.path.isdir(f"include/{old_lib_name}"):
        os.rename(f"include/{old_lib_name}", f"include/{new_lib_name}")
        print(f"Renamed directory: include/{old_lib_name} to include/{new_lib_name}")

    print("Project renaming completed.")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python3 SolutionRenamer.py <old_lib_name> <new_lib_name> <old_standalone_name> <new_standalone_name>")
        sys.exit(1)

    old_lib_name = sys.argv[1]
    new_lib_name = sys.argv[2]
    old_standalone_name = sys.argv[3]
    new_standalone_name = sys.argv[4]

    rename_project(old_lib_name, new_lib_name, old_standalone_name, new_standalone_name)
    
# Copyright (c) 2024 Tomáš Mark