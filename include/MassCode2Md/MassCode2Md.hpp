#ifndef __MASSCODE2MD_H__
#define __MASSCODE2MD_H__

#include <string>

class MassCode2Md
{
  public:
    MassCode2Md();
    ~MassCode2Md();

    int parser(std::string dbJsonPath, std::string mdOutputPath);

  private:
};

#endif // __MASSCODE2MD_H__