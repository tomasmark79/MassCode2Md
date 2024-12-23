#include <MassCode2Md/MassCode2Md.hpp>
#include <masscode2md/version.h>

#include <chrono>
#include <iostream>
#include <memory>
#include <thread>

// Standalone main entry point

auto main(int argc, char *argv[], char *env[]) -> int
{
    // init MassCode2Md instance
    std::unique_ptr<MassCode2Md> Lib = std::make_unique<MassCode2Md>();

    // db.json
    // const std::string dbJsonPath =
    //     "/home/tomas/dev/cpp/projects/MassCode2Md/input/db.json";

    // // output folder for markdown files
    // const std::string mdOutputPath =
    //     "/home/tomas/dev/cpp/projects/MassCode2Md/output";

    // usage
    if (argc != 3)
    {
        std::cout << "Usage: " << argv[0] << " <db.json> <output_folder>\n"
                  << std::endl;
        return 1;
    }

    // get input and output from command line
    if (argc == 3)
    {
        
        // db.json
        const std::string dbJsonPath = argv[1];

        // output folder for markdown files
        const std::string mdOutputPath = argv[2];

        // parse db.json
        Lib->parser(dbJsonPath, mdOutputPath);
    }

    // five seconds delay
    std::cout << "Wait for 5 seconds please ..." << std::endl;
    std::this_thread::sleep_for(std::chrono::seconds(5));

    // bye bye
    std::cout << "Bye bye!" << std::endl;

    return 0;
}
