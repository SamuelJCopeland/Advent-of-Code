#include "day2.hpp"

#include <fstream>
#include <iostream>

#include "stringParser.hpp"

void Day2::Run(const std::string& aPath)
{
   std::fstream inFile;
   inFile.open(aPath, std::ios::in);

   if (!inFile.is_open())
   {
      std::cout << "Could not open file: " << aPath << std::endl;
      return;
   }

   std::string line;

   while (std::getline(inFile, line)){}
}
