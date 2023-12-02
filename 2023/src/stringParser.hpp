#ifndef STRINGPARSER_HPP
#define STRINGPARSER_HPP

#include <vector>
#include <string>

class StringParser
{
public:
   static std::vector<std::string> Split(const std::string& aInput, const std::string& aSplit = " ");
};

#endif /* STRINGPARSER_HPP */