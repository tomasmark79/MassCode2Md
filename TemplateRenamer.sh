#!/bin/bash

# This script rename the Standalone and Library names in the template 
# (c) Tomáš Mark 2024

# Check if four arguments are provided
if [ "$#" -ne 4 ]; then
    echo "Usage: $0 <old_lib_name> <new_lib_name> <old_standalone_name> <new_standalone_name>"
    exit 1
fi

# Assign arguments to variables
old_lib_name=$1
new_lib_name=$2
old_standalone_name=$3
new_standalone_name=$4

# Convert to lowercase and uppercase
old_lib_name_lower=$(echo "$old_lib_name" | tr '[:upper:]' '[:lower:]')
new_lib_name_lower=$(echo "$new_lib_name" | tr '[:upper:]' '[:lower:]')
old_lib_name_upper=$(echo "$old_lib_name" | tr '[:lower:]' '[:upper:]')
new_lib_name_upper=$(echo "$new_lib_name" | tr '[:lower:]' '[:upper:]')


# new_lib_name and new_standalone_name has not to be same
if [ "$new_lib_name" == "$new_standalone_name" ]; then
    echo "Error: new_lib_name and new_standalone_name has to be different"
    exit 1
fi

# List of files where the project names should be changed
files=(
    ".vscode/launch.json"
    "LICENSE"
    "CMakeLists.txt"
    "include/$old_lib_name/$old_lib_name.hpp"
    "Source/$old_lib_name.cpp"
    "Standalone/CMakeLists.txt"
    "Standalone/Source/Main.cpp"
    # Add more files as needed
)

# Replace the old library name with the new one in each file
for file in "${files[@]}"; do
    if [ -f "$file" ]; then

        sed -i "s/$old_lib_name/$new_lib_name/g" "$file"
        sed -i "s/$old_standalone_name/$new_standalone_name/g" "$file"

        sed -i "s/$old_lib_name_lower/$new_lib_name_lower/g" "$file"
        sed -i "s/$old_lib_name_upper/$new_lib_name_upper/g" "$file"

        echo "Renamed project names in file: $file"
    else
        echo "File $file does not exist!"
    fi
done

# Rename files
if [ -f "Source/$old_lib_name.cpp" ]; then
    mv "Source/$old_lib_name.cpp" "Source/$new_lib_name.cpp"
    echo "Renamed file: Source/$old_lib_name.cpp to Source/$new_lib_name.cpp"
fi

if [ -f "include/$old_lib_name/$old_lib_name.hpp" ]; then
    mv "include/$old_lib_name/$old_lib_name.hpp" "include/$old_lib_name/$new_lib_name.hpp"
    echo "Renamed file: include/$old_lib_name/$old_lib_name.hpp to include/$old_lib_name/$new_lib_name.hpp"
fi

# Rename directories
if [ -d "include/$old_lib_name" ]; then
    mv "include/$old_lib_name" "include/$new_lib_name"
    echo "Renamed directory: include/$old_lib_name to include/$new_lib_name"
fi

echo "Project renaming completed."
