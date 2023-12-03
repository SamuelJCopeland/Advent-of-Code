#include "day2.hpp"

#include <fstream>
#include <iostream>
#include <sstream>

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
   int gameSum = 0;
   int powerSum = 0;

   while (std::getline(inFile, line))
   {
      int maxRed = 12;
      int maxBlue = 14;
      int maxGreen = 13;

      // Separate on space
      auto spaceSplit = StringParser::Split(line);
      std::string game = spaceSplit.at(1);
      auto gameSplit = StringParser::Split(game, ":");
      int gameNum;
      std::stringstream ss;
      ss << gameSplit.at(0);
      ss >> gameNum;
      
      std::cout << "GameNum: " << gameNum << std::endl;

      bool fits = true;
      int minRed = 0;
      int minGreen = 0;
      int minBlue = 0;

      for (const auto& round : StringParser::Split(StringParser::Split(line, ":").at(1), ";"))
      {
         int redTotal = 0;
         int blueTotal = 0;
         int greenTotal = 0;

         std::cout << round << std::endl;
         for (const auto& colorSet : StringParser::Split(round, ", "))
         {
            int quantity;
            auto color = StringParser::Split(colorSet).at(1);

            std::stringstream ss;
            auto q = StringParser::Split(colorSet).at(0);
            ss << q;
            ss >> quantity;

            if (color == "red")
            {
               redTotal += quantity;

               if (quantity > minRed)
               {
                  minRed = quantity;
               }
            }
            else if (color == "green")
            {
               greenTotal += quantity;

               if (quantity > minGreen)
               {
                  minGreen = quantity;
               }
            }
            else
            {
               blueTotal += quantity;

               if (quantity > minBlue)
               {
                  minBlue = quantity;
               }
            }
         }

         if (!(redTotal <= maxRed && blueTotal <= maxBlue && greenTotal <= maxGreen))
         {
            fits = false;
            std::cout << "Doesn't fit" << std::endl;
         }
         std::cout << "Red: " << redTotal << " Green: " << greenTotal << " Blue: " << blueTotal << std::endl;
      }

      if (fits)
      {
         gameSum += gameNum;
      }
      std::cout << "Power: " << minRed * minGreen * minBlue << std::endl;

      powerSum += minRed * minGreen * minBlue;
   }
   std::cout << "Game Sum: " << gameSum << std::endl;
   std::cout << "Power Sum: " << powerSum << std::endl;
}
