import os
import requests
import shutil
from datetime import datetime
import sys
import subprocess
import tempfile
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Use temp directory for lock file
lock_file = os.path.join(tempfile.gettempdir(), "SolutionUpgrader.lock")

# URL of the repository with the updated files
repo_url = "https://raw.githubusercontent.com/tomasmark79/MarkWareVCMake/refs/heads/main/"

files_to_update = [
    # "cmake/Modules/FindX11.cmake",
    # "cmake/CPM.cmake",
    # "cmake/tools.cmake",
    # ".github/workflows/install.yml",
    # ".github/workflows/macos.yml",
    # ".github/workflows/ubuntu.yml",
    # ".github/workflows/windows.yml",
    # "include/VCMLib/VCMLib.hpp",
    # "Source/VCMLib.cpp",
    # "Standalone/Source/Main.cpp",
    # "Standalone/CMakeLists.txt",
    # "Standalone/LICENSE",
    # "Utilities/CMakeToolChains/aarch64-linux-gnu.cmake",
    # "Utilities/CMakeToolChains/x86_64-unknown-linux-gnu.cmake",
    # "Utilities/CMakeToolChains/x86_64-w64-mingw32.cmake",
    # "Utilities/ConanProfiles/aarch64-linux-gnu",
    # "Utilities/ConanProfiles/x86_64-unknown-linux-gnu",
    # "Utilities/ConanProfiles/x86_64-w64-mingw32",
    # "Utilities/AboutThisFolder.md",
    # ".vscode/c_cpp_properties.json",
    # ".vscode/keybindings.json",
    # ".vscode/launch.json",
    # ".vscode/settings.json",
    # ".vscode/tasks.json",
    # ".clang-format",
    # ".cmake-format",
    # "CMakeLists.txt",
    # "conanfile.py",
    # ".gitattributes",
    # ".gitignore",
    # "LICENSE",
    # ".python-version",
    # "README.md",
    # "SolutionController.py",
    # "SolutionRenamer.py",
    "SolutionUpgrader.py"
]

def check_write_permissions(path):
    try:
        test_file = os.path.join(os.path.dirname(path) or '.', '.write_test')
        with open(test_file, 'w') as f:
            f.write('test')
        os.remove(test_file)
        return True
    except (IOError, OSError):
        return False

def create_backup_dir():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    backup_dir = os.path.join("backup", timestamp)
    os.makedirs(backup_dir, exist_ok=True)
    return backup_dir

def can_update_file(file_path):
    # Always allow self-update
    if file_path == "SolutionUpgrader.py":
        return True
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                if "<VCMAKE_NO_UPDATE>" in line:
                    return False
    except UnicodeDecodeError:
        with open(file_path, 'r') as file:
            for line in file:
                if "<VCMAKE_NO_UPDATE>" in line:
                    return False
    return True

def update_file(file_path, backup_dir):
    if not check_write_permissions(file_path):
        logging.error(f"No write permissions for {file_path}")
        return False

    try:
        url = repo_url + file_path
        response = requests.get(url, timeout=30, verify=True)
        response.raise_for_status()

        # Backup existing file
        if os.path.exists(file_path) and file_path != "SolutionUpgrader.py":
            backup_path = os.path.join(backup_dir, file_path)
            os.makedirs(os.path.dirname(backup_path), exist_ok=True)
            shutil.copy2(file_path, backup_path)
            logging.info(f"Backed up: {file_path}")

        # Create directory if needed
        dir_name = os.path.dirname(file_path)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)

        # Try UTF-8 first, fallback to detected encoding
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(response.text)
            logging.info(f"Updated: {file_path}")
        except UnicodeEncodeError:
            with open(file_path, 'w', encoding=response.encoding) as file:
                file.write(response.text)
            logging.info(f"Updated with {response.encoding} encoding: {file_path}")
        return True

    except requests.RequestException as e:
        logging.error(f"Failed to update {file_path}: {str(e)}")
    except OSError as e:
        logging.error(f"File system error for {file_path}: {str(e)}")
    return False

def restart_script():
    logging.info("Restarting script...")
    if sys.platform.startswith('win'):
        subprocess.Popen([sys.executable] + sys.argv, shell=True)
    else:
        subprocess.Popen([sys.executable] + sys.argv)
    sys.exit(0)

def main():
    if os.path.exists(lock_file):
        os.remove(lock_file)
        logging.info("Lock file removed")
        return

    backup_dir = None
    updated_self = False

    for file_path in files_to_update:
        if os.path.exists(file_path):
            if can_update_file(file_path):
                logging.info(f"Updating: {file_path}")
                
                # Vytvoř backup_dir pouze když je potřeba zálohovat
                if file_path != "SolutionUpgrader.py" and backup_dir is None:
                    backup_dir = create_backup_dir()
                
                # Update souboru
                if update_file(file_path, backup_dir):
                    if file_path == "SolutionUpgrader.py":
                        updated_self = True
            else:
                logging.info(f"Skipped (protected): {file_path}")
        else:
            logging.info(f"Creating new file: {file_path}")
            if backup_dir is None:
                backup_dir = create_backup_dir()
            update_file(file_path, backup_dir)

    if updated_self:
        with open(lock_file, 'w') as f:
            f.write("lock")
        restart_script()

if __name__ == "__main__":
    main()
