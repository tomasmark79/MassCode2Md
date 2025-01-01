#include "MassCode2Md/MassCode2Md.hpp"

#include <algorithm>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <masscode2md/version.h>
#include <nlohmann/json.hpp>
#include <regex>
#include <string>
#include <utility>
#include <vector>

MassCode2Md::MassCode2Md()
{
    std::cout << "--- MassCode2Md v." << MASSCODE2MD_VERSION << " instantiated ---" << std::endl;
}

MassCode2Md::~MassCode2Md()
{
    std::cout << "--- MassCode2Md uninstantiated ---" << std::endl;
}

/// @brief Load db.json file and parse it to markdown files
/// @param dbJsonPath
/// @param mdOutputPath
/// @return 0 if success
int MassCode2Md::parser(std::string dbJsonPath, std::string mdOutputPath)
{
    std::cout << "Parsing db.json file:\t" << dbJsonPath << std::endl;
    std::cout << "Output file:\t\t" << mdOutputPath << std::endl;

    int totalWrittenFolders = 0;
    int totalWrittenFiles = 0;

    // Load file to buffer

    if (!std::filesystem::exists(dbJsonPath))
    {
        std::cout << "Input file does not exist: " << dbJsonPath << std::endl;
        return 1;
    }

    std::ifstream dbJsonFile(dbJsonPath); // Open file
    std::string   dbJsonContent(
        (std::istreambuf_iterator<char>(dbJsonFile)),
        std::istreambuf_iterator<char>()
    ); // Read file to string

    nlohmann::json dbJson;
    try
    {
        dbJson = nlohmann::json::parse(dbJsonContent); // Parse JSON
    }
    catch (const std::exception &e)
    {
        std::cerr << e.what() << '\n';
        return 1;
    }

    // Create Folders
    std::vector<std::pair<std::string, std::string>> folderData;
    for (const auto &folders : dbJson["folders"])
    {
        std::string folderName = folders["name"];
        std::string folderId = folders["id"];

        folderData.push_back(std::make_pair(folderName, folderId));

        // Create the folder using the folderName
        std::cout << "Folder Name: " << folderName << ", Folder ID: " << folderId << std::endl;

        // Replace invalid characters in label with a valid character
        std::replace_if(
            folderName.begin(),
            folderName.end(),
            [](char c) { return !std::isalnum(c) && c != '_' && c != '-' && c != '+'; },
            '_'
        );

        std::string folderPath = mdOutputPath + "/" + folderName;
        if (std::filesystem::exists(folderPath))
        {
            std::cout << "Folder already exists: " << folderPath << std::endl;
            // Update the folderName in the folderData vector
            folderData.back().first = folderName;
            continue;
        }
        else
        {
            std::cout << "Creating folder: " << folderPath << std::endl;
            if (!std::filesystem::create_directory(folderPath))
            {
                std::cout << "Failed to create folder: " << folderPath << std::endl;
                return 1;
            }
            totalWrittenFolders++;
        }

        // Update the folderName in the folderData vector
        folderData.back().first = folderName;
    }

    // Process the Snippets --------------------------------------------------
    for (const auto &snippet : dbJson["snippets"])
    {
        // skip deleted snippets
        if (snippet["isDeleted"])
            continue;

        std::string folderId = snippet["folderId"];
        std::string name = snippet["name"];

        // Print the snippet data
        std::cout << "Snippet: " << name << ", Folder ID: " << folderId << std::endl;

        // Find the folderName for this folderId
        std::string folderName;
        for (const auto &folder : folderData)
        {
            if (folder.second == folderId)
            {
                folderName = folder.first;
                break;
            }
        }

        if (folderName.empty())
        {
            std::cout << "Failed to find folder for snippet: "
                      << snippet["label"].get<std::string>() << std::endl;
            continue;
        }

        // Process each content in the snippet and add id of the content to the
        // end of the file name
        int id = 0;
        int fragmentId = 0;
        for (const auto &content : snippet["content"])
        {
            int fragmentCount = snippet["content"].size();

            std::string label = content["label"];
            std::string value = content["value"];
            std::string language = content["language"];

            if (label.empty() || value.empty())
            {
                std::cout << "Invalid content in snippet: " << snippet["name"].get<std::string>()
                          << std::endl;
                continue;
            }

            // Replace invalid characters in label with a valid character
            std::replace_if(
                name.begin(),
                name.end(),
                [](char c) { return !std::isalnum(c) && c != '_' && c != '-' && c != '+'; },
                '_'
            );

            // Create the file name depending on the id
            if (id > 0)
            {
                name = name + "_" + std::to_string(id);
            }

            std::string filePath = "";
            if (fragmentCount > 1)
            {
                filePath = mdOutputPath + "/" + folderName + "/" + name + "_" +
                    std::to_string(fragmentId + 1) + "_from_" + std::to_string(fragmentCount) +
                    ".md";
                fragmentId++;
            }
            else
            {
                filePath = mdOutputPath + "/" + folderName + "/" + name + ".md";
            }

            // check if file is existing
            if (std::filesystem::exists(filePath))
            {
                std::cout << "File already exists: " << filePath << std::endl;
                continue;
            }
            else
            {
                std::cout << "Creating file: " << filePath << std::endl;
                std::ofstream outFile(filePath); // Open file
                if (!outFile)
                {
                    std::cout << "Failed to create file: " << filePath << std::endl;
                    continue;
                }
                totalWrittenFiles++;

                // Change the language to cpp if it is c_cpp to match the
                // markdown language
                if (language == "c_cpp")
                {
                    language = "cpp";
                }

                outFile << "```" << language << '\n';
                outFile << value;
                outFile << '\n' << "```" << '\n';

                outFile.close();
            }
        }
    }

    std::cout << "Total written folders:\t" << totalWrittenFolders << std::endl;
    std::cout << "Total written files:\t" << totalWrittenFiles << std::endl;

    std::cout << "Parsing done!" << std::endl;

    return 0;
}