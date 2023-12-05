#include "day4.hpp"

#include <iostream>
#include <sstream>
#include <vector>
#include <fstream>

#include "stringParser.hpp"

void Day4::Run(const std::string& aPath)
{
   std::fstream inFile;
   inFile.open(aPath, std::ios::in);

   if (!inFile.is_open())
   {
      std::cout << "Could not open file: " << aPath << std::endl;
      return;
   }

   std::string line;
   std::vector<std::string> lines;

   while (std::getline(inFile, line))
   {
      lines.push_back(line);
   }

   int totalPoints = 0;

   for (const auto& line : lines)
   {
      ScratchCard card;
      std::string cardNumberString =
         StringParser::Split(StringParser::Split(line, ": ").at(0)).at(1);
      std::string cardNums = StringParser::Split(line, ": ").at(1);

      std::stringstream ss;
      ss << cardNumberString;
      ss >> card.mNumber;

      // Left side is numbers you have, Right side is winning numbers.
      auto left = StringParser::Split(cardNums, " | ").at(0);
      auto right = StringParser::Split(cardNums, " | ").at(1);

      int points = 0;
      int matches = 0;

      for (const auto& leftNum : StringParser::Split(left))
      {
         for (const auto& rightNum : StringParser::Split(right))
         {
            if (leftNum == rightNum)
            {
               if (points == 0)
               {
                  points += 1;
               }
               else
               {
                  points *= 2;
               }

               ++matches;
            }
         }         
      }

      totalPoints += points;
      card.mPoints = matches;
      mCards.push_back(card);
   }

   int cardCount = mCards.size();

   for (const auto& card : mCards)
   {
      if (card.mPoints > 0)
      {
         for (size_t i = 0; i < card.mPoints; ++i)
         {
            mCardQueue.push(mCards.at(i + card.mNumber));
            ++cardCount;
         }
      }

      while (!mCardQueue.empty())
      {
         auto qCard = mCardQueue.front();
         mCardQueue.pop();

         if (qCard.mPoints > 0)
         {
            for (size_t i = 0; i < qCard.mPoints; ++i)
            {
               mCardQueue.push(mCards.at(i + qCard.mNumber));
               ++cardCount;
            }
         }
      }
   }

   std::cout << "Part 1: " << totalPoints << std::endl;
   std::cout << "Part 2: " << cardCount << std::endl;
}
