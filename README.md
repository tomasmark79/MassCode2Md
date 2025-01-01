# MassCode2Md

Author: **Tomáš Mark**  
Version: **main**

[![Ubuntu](https://github.com/tomasmark79/MassCode2Md/actions/workflows/ubuntu.yml/badge.svg)](https://github.com/tomasmark79/MassCode2Md/actions/workflows/ubuntu.yml)
[![MacOS](https://github.com/tomasmark79/MassCode2Md/actions/workflows/macos.yml/badge.svg)](https://github.com/tomasmark79/MassCode2Md/actions/workflows/macos.yml)
[![Windows](https://github.com/tomasmark79/MassCode2Md/actions/workflows/windows.yml/badge.svg)](https://github.com/tomasmark79/MassCode2Md/actions/workflows/windows.yml)

MassCode2Md is a lightweight tool designed to convert code snippets stored in JSON format into organized Markdown files. The tool reads a JSON file containing code snippets and automatically arranges them into directories based on the provided structure in the JSON file.

Please note that the program does not include robust controls and checks, so ensure that you pass the correct arguments. The output folder must exist before generating Markdown files.

### Usage

To use MassCode2Md, run the following command:

```bash
./MassCode2MdStandalone <db.json> <output_folder>
```

#### Example

```bash
./MassCode2MdStandalone db.json ./out
```

Set the paths and run the command. That's all you need to do.

---

**[MarkWareVCMake](https://github.com/tomasmark79/MarkWareVCMake)** – Kickstart your next project with this CMake template. ✨ It features a well-structured layout, integration of modern C++ standards, and a focus on cross-platform compatibility. Ideal for both beginners and experienced developers. 💻
