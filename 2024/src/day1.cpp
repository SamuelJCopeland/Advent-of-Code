#include "day1.hpp"

#include <fstream>
#include <iostream>
#include <sstream>
#include <cmath>
#include "stringParser.hpp"

void Day1::MakeLists(const std::string& aPath)
{

   std::fstream inFile;
   inFile.open(aPath, std::ios::in);

   if (!inFile.is_open())
   {
      std::cout << "Could not open file: " << aPath << std::endl;
      return;
   }

   std::string line;

   while (std::getline(inFile, line))
   {
      int int1, int2;
      auto splitNums = StringParser::Split(line, "   ");

      int1 = std::stoi(splitNums.at(0));
      int2 = std::stoi(splitNums.at(1));

      mList1.push_back(int1);
      mList2.push_back(int2);
   }

   Sort(mList1);
   Sort(mList2);
}

void Day1::Sort(std::vector<int>& aList)
{
   for (size_t i = 0; i < aList.size(); ++i)
   {
      for (size_t j = i + 1; j < aList.size(); ++j)
      {
         if (aList.at(i) > aList.at(j))
         {
            int temp = aList.at(i);
            aList.at(i) = aList.at(j);
            aList.at(j) = temp;
         }
      }
   }
}

void Day1::Part1(const std::string& aPath)
{
   if (mList1.empty())
   {
      MakeLists(aPath);
   }

   int sum = 0;

   for (size_t i = 0; i < mList1.size(); ++i)
   {
      //std::cout << mList1.at(i) << " " << mList2.at(i) << std::endl;
      sum += abs(mList1.at(i) - mList2.at(i));
   }

   std::cout << sum << std::endl;
}

void Day1::Part2(const std::string& aPath)
{
   if (mList1.empty())
   {
      MakeLists(aPath);
   }
   
   int sum = 0;

   for (size_t i = 0; i < mList1.size(); ++i)
   {
      int count = 0;
      int num = mList1.at(i);

      for (size_t j = 0; j < mList2.size(); ++j)
      {
         if (mList2.at(j) == num)
         {
            ++count;
         }
      }

      sum += count * num;
   }

   std::cout << sum << std::endl;
}
