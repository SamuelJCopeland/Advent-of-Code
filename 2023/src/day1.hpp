#ifndef DAY1_HPP
#define DAY1_HPP

#include <string>

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
   void Run(const std::string& aPath);
private:
};

#endif