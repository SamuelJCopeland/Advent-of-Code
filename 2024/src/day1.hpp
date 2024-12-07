#ifndef DAY1_HPP
#define DAY1_HPP

#include <string>
#include <vector>

enum class State
{
   START = 0,
   O  = 1,
   T  = 2,
   TH = 3,
   TW = 4,
   F  = 5,
   FO = 6,
   FI = 7,
   S  = 8,
   SI = 9,
   SE = 10,
   E  = 11,
   N  = 12
};

class Day1
{
public:
   void Part1(const std::string& aPath);
   void Part2(const std::string& aPath);
private:
   std::vector<int> mList1;
   std::vector<int> mList2;

   void MakeLists(const std::string& aPath);
   void Sort(std::vector<int>& aList);
};

#endif