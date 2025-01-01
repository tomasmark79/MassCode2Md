
#include <MassCode2Md/MassCode2Md.hpp>
#include <masscode2md/version.h>

#include <chrono>
#include <iostream>
#include <memory>
#include <thread>

int main(int argc, char *argv[])
{
    std::unique_ptr<MassCode2Md> Lib = std::make_unique<MassCode2Md>(); // cpp14 +
    // std::unique_ptr<MassCode2Md> Lib(new MassCode2Md()); // cpp11 +

    // usage
    if (argc != 3)
    {
        std::cout << "Usage: " << argv[0] << " <db.json> <output_folder>\n" << std::endl;
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

    // remove me ------------------👇🏻
    std::cout << "Wait for 5 seconds please ..." << std::endl;
    std::this_thread::sleep_for(std::chrono::seconds(5));
    std::cout << "Bye bye!" << std::endl;
    // remove me ------------------👆🏻

    return 0;
}
