#ifndef DAY3_HPP
#define DAY3_HPP

#include <string>
#include <vector>

struct PartNumber
{
   int    mNumber     { 0 };
   size_t mRow        { 0 };
   size_t mColStart   { 0 };
   size_t mColEnd     { 0 };
   std::vector<std::pair<size_t, size_t>> mStarLocs;
   bool   mIsAdjacent{ false };
};

class Day3
{
public:
   void Run(const std::string& aPath);
};

#endif /* DAY3_HPP */