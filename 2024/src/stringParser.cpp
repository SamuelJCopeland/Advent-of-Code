#include "stringParser.hpp"

std::vector<std::string> StringParser::Split(const std::string& aInput, const std::string& aSplit)
{
   std::vector<std::string> result;

   std::string current;

   for (size_t i = 0; i < aInput.size(); ++i)
   {
      bool match = true;

      // Check to see if it matches the split string.
      for (size_t j = 0; i + j < aInput.size() && j < aSplit.size(); ++j)
      {
         if (aInput[i + j] != aSplit[j])
         {
            match = false;
            break;
         }
      }

      if (match)
      {
         if (current != "")
         {
            result.push_back(current);
         }

         current = "";
         i += aSplit.size() - 1;
      }
      else
      {
         current += aInput[i];
      }
   }

   if (current != "")
   {
      result.push_back(current);
   }

   return result;
}
