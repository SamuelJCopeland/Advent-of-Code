#ifndef DAY5_HPP
#define DAY5_HPP

#include <string>
#include <vector>
#include <unordered_map>

struct AlmanacMap
{
   unsigned int mDest{ 0 };
   unsigned int mSrc{ 0 };
   unsigned int mLength{ 0 };
};

class Day5
{
public:
   void Run(const std::string& aPath);

private:
   std::unordered_map<std::string, std::vector<AlmanacMap>> mMaps;
   std::vector<unsigned int>                                mSeeds;

   unsigned int Part1();
   std::vector<unsigned int> Part1Helper(const std::vector<unsigned int>& aSrcs, const std::string& aKey);

   unsigned int Part2();
};

#endif /* DAY5_HPP */