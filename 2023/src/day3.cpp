#include "day3.hpp"

#include <fstream>
#include <iostream>
#include <vector>
#include <sstream>

void Day3::Run(const std::string& aPath)
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

   std::vector<PartNumber> partNumbers;

   for (size_t i = 0; i < lines.size(); ++i)
   {
      std::string numString{ "" };
      PartNumber partNum;

      for (size_t j = 0; j < lines.at(i).size(); ++j)
      {
         if (std::isdigit(lines.at(i).at(j)))
         {
            if (numString == "")
            {
               partNum.mRow = i;
               partNum.mColStart = j;
            }

            numString += lines.at(i).at(j);
         }
         else if (numString.size() > 0)
         {
            if (lines.at(i).at(j) != '.')
            {
               partNum.mIsAdjacent = true;
               
               if (lines.at(i).at(j) == '*')
               {
                  partNum.mStarLocs.push_back(std::pair<size_t, size_t>(i, j));
               }
            }

            std::stringstream ss;
            ss << numString;
            ss >> partNum.mNumber;
            numString = "";
            partNum.mColEnd = j - 1;
            partNumbers.push_back(partNum);
            partNum = PartNumber();

         }
      }

      if (numString != "")
      {
         std::stringstream ss;
         ss << numString;
         ss >> partNum.mNumber;
         numString = "";
         partNum.mColEnd = lines.at(i).size() - 1;
         partNumbers.push_back(partNum);
         partNum = PartNumber();
      }
   }

   for (auto& partNumber : partNumbers)
   {
      // Check on the left side.
      if (partNumber.mColStart > 0)
      {
         if (lines.at(partNumber.mRow).at(partNumber.mColStart - 1) != '.')
         {
            partNumber.mIsAdjacent = true;

            if (lines.at(partNumber.mRow).at(partNumber.mColStart - 1) == '*')
            {
               partNumber.mStarLocs.push_back(std::pair<size_t, size_t>(partNumber.mRow, partNumber.mColStart - 1));
            }
         }
      }

      // I don't need to check the right side because it was already checked.

      // Check the above row.
      if (partNumber.mRow > 0)
      {
         if (partNumber.mColStart > 0)
         {
            for (size_t i = partNumber.mColStart - 1; i <= partNumber.mColEnd + 1
               && i < lines.at(partNumber.mRow - 1).size(); ++i)
            {
               if ((!std::isdigit(lines.at(partNumber.mRow - 1).at(i)))
                  && lines.at(partNumber.mRow - 1).at(i) != '.')
               {
                  partNumber.mIsAdjacent = true;

                  if (lines.at(partNumber.mRow - 1).at(i) == '*')
                  {
                     partNumber.mStarLocs.push_back(std::pair<size_t, size_t>(partNumber.mRow - 1, i));
                  }
               }
            }
         }
         else
         {
            for (size_t i = partNumber.mColStart; i <= partNumber.mColEnd + 1
               && i < lines.at(partNumber.mRow - 1).size(); ++i)
            {
               if ((!std::isdigit(lines.at(partNumber.mRow - 1).at(i)))
                  && lines.at(partNumber.mRow - 1).at(i) != '.')
               {
                  partNumber.mIsAdjacent = true;

                  if (lines.at(partNumber.mRow - 1).at(i) == '*')
                  {
                     partNumber.mStarLocs.push_back(std::pair<size_t, size_t>(partNumber.mRow - 1, i));
                  }
               }
            }
         }
      }

      // Check the below row.
      if (partNumber.mRow + 1 < lines.size())
      {
         if (partNumber.mColStart > 0)
         {
            for (size_t i = partNumber.mColStart - 1; i <= partNumber.mColEnd + 1
               && i < lines.at(partNumber.mRow + 1).size(); ++i)
            {
               if ((!std::isdigit(lines.at(partNumber.mRow + 1).at(i)))
                  && lines.at(partNumber.mRow + 1).at(i) != '.')
               {
                  partNumber.mIsAdjacent = true;

                  if (lines.at(partNumber.mRow + 1).at(i) == '*')
                  {
                     partNumber.mStarLocs.push_back(std::pair<size_t, size_t>(partNumber.mRow + 1, i));
                  }

               }
            }
         }
         else
         {
            for (size_t i = partNumber.mColStart; i <= partNumber.mColEnd + 1
               && i < lines.at(partNumber.mRow + 1).size(); ++i)
            {
               if ((!std::isdigit(lines.at(partNumber.mRow + 1).at(i)))
                  && lines.at(partNumber.mRow + 1).at(i) != '.')
               {
                  partNumber.mIsAdjacent = true;

                  if (lines.at(partNumber.mRow + 1).at(i) == '*')
                  {
                     partNumber.mStarLocs.push_back(std::pair<size_t, size_t>(partNumber.mRow + 1, i));
                  }
               }
            }
         }
      }

   }

   int sumPartNums = 0;
   int sumGearRatios = 0;
   std::vector<std::pair<size_t, size_t>> foundStars;

   for (const auto& partNum : partNumbers)
   {

      for (auto star : partNum.mStarLocs)
      {
         int ratio = 1;
         int count = 0;
         bool alreadyFound = false;

         // Make sure that this star wasn't already found.
         for (auto fStar : foundStars)
         {
            if (fStar.first == star.first && fStar.second == star.second)
            {
               alreadyFound = true;
               break;
            }
         }

         if (alreadyFound)
         {
            continue;
         }
         else
         {
            foundStars.push_back(star);
         }

         // Find all instances of that star loc
         for (const auto& part : partNumbers)
         {
            for (auto pStar : part.mStarLocs)
            {
               if (pStar.first == star.first && pStar.second == star.second)
               {
                  ratio *= part.mNumber;
                  ++count;
               }
            }
         }

         if (count == 2)
         {
            sumGearRatios += ratio;
         }
      }

      if (partNum.mIsAdjacent)
      {
         sumPartNums += partNum.mNumber;
      }
   }



   std::cout << "Part 1: " << sumPartNums << std::endl;
   std::cout << "Part 2: " << sumGearRatios << std::endl;
}
