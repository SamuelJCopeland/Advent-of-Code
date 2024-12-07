#include "day5.hpp"

#include <vector>
#include <fstream>
#include <sstream>
#include <iostream>

#include "stringParser.hpp"

void Day5::Run(const std::string& aPath)
{
   std::fstream inFile;
   inFile.open(aPath, std::ios::in);

   if (!inFile.is_open())
   {
      std::cout << "Could not open file: " << aPath << std::endl;
      return;
   }

   std::string line;
   std::string curKey;

   // Parse the first line, this is the line that contains the list of seeds.
   std::getline(inFile, line);
   auto seedLine = StringParser::Split(line);

   for (size_t i = 1; i < seedLine.size(); ++i)
   {
      unsigned int seed;
      std::stringstream ss;
      ss << seedLine.at(i);
      ss >> seed;
      mSeeds.push_back(seed);
   }

   while (std::getline(inFile, line))
   {
      if (line == "")
      {
         continue;
      }

      if (!std::isdigit(StringParser::Split(line).at(0).at(0)))
      {
         curKey = StringParser::Split(line).at(0);
      }
      else
      {
         // Put the numbers in the line into an AlmanacMap and place it in mMaps.
         if (mMaps.find(curKey) == mMaps.end())
         {
            mMaps[curKey] = std::vector<AlmanacMap>();
         }

         std::stringstream ss;
         AlmanacMap map;

         ss << StringParser::Split(line).at(0);
         ss >> map.mDest;
         ss.clear();
         ss << StringParser::Split(line).at(1);
         ss >> map.mSrc;
         ss.clear();
         ss << StringParser::Split(line).at(2);
         ss >> map.mLength;

         mMaps.at(curKey).push_back(map);
      }
   }

   std::cout << "Part 1: " << Part1() << std::endl;
}

unsigned int Day5::Part1()
{
   std::vector<unsigned int> soils = Part1Helper(mSeeds, "seed-to-soil");

   std::vector<unsigned int> fertilizers = Part1Helper(soils, "soil-to-fertilizer");

   std::vector<unsigned int> waters = Part1Helper(fertilizers, "fertilizer-to-water");

   std::vector<unsigned int> lights = Part1Helper(waters, "water-to-light");

   std::vector<unsigned int> temperatures = Part1Helper(lights, "light-to-temperature");

   std::vector<unsigned int> humidities = Part1Helper(temperatures, "temperature-to-humidity");

   std::vector<unsigned int> locations = Part1Helper(humidities, "humidity-to-location");

   unsigned int min = 999999999999999;

   for (unsigned int location : locations)
   {
      if (location < min)
      {
         min = location;
      }
   }

   return min;
}

std::vector<unsigned int> Day5::Part1Helper(const std::vector<unsigned int>& aSrcs, const std::string& aKey)
{
   std::vector<unsigned int> destinations;

   for (unsigned int src : aSrcs)
   {
      bool found = false;

      for (auto map : mMaps.at(aKey))
      {
         if (src >= map.mSrc && src < map.mSrc + map.mLength)
         {
            found = true;
            destinations.push_back(map.mDest + src - map.mSrc);
            break;
         }
      }

      if (!found)
      {
         destinations.push_back(src);
      }
   }

   return destinations;
}

unsigned int Day5::Part2()
{
   // Work backwards. Start with the lowest locations and try to find a seed that correlates.
}
