#ifndef DAY4_HPP
#define DAY4_HPP

#include <string>
#include <vector>
#include <queue>

struct ScratchCard
{
   int mNumber{ 0 };
   int mPoints{ 0 };
};

class Day4
{
public:
   void Run(const std::string& aPath);

private:
   std::vector<ScratchCard> mCards;
   std::queue<ScratchCard>  mCardQueue;
};

#endif /* DAY4_HPP */