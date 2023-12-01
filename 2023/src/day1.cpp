#include "day1.hpp"

#include <fstream>
#include <iostream>
#include <sstream>

void Day1::Run(const std::string& aPath)
{
   std::fstream inFile;
   inFile.open(aPath, std::ios::in);

   if (!inFile.is_open())
   {
      std::cout << "Could not open file: " << aPath << std::endl;
      return;
   }

   std::string line;
   int sum = 0;

   while (std::getline(inFile, line))
   {
      char firstChar = 'a';
      char lastChar = 'a';
      int length{ 0 };
      State state = State::START;

      for (size_t i = 0; i < line.size(); ++i)
      {
         char c = line[i];

         if (std::isdigit(c))
         {
            state = State::START;
            length = 0;

            if (firstChar == 'a')
            {
               firstChar = c;
            }
            else
            {
               lastChar = c;
            }
         }
         else
         {
            switch (state)
            {
            case State::START:
               switch (c)
               {
               case 'o':
                  length++;
                  state = State::O;
                  break;
               case 't':
                  length++;
                  state = State::T;
                  break;
               case 'f':
                  length++;
                  state = State::F;
                  break;
               case 's':
                  length++;
                  state = State::S;
                  break;
               case 'e':
                  length++;
                  state = State::E;
                  break;
               case 'n':
                  length++;
                  state = State::N;
               default:
                  break;
               }
               break;
            case State::O:
               switch (length)
               {
               case 1:
                  if (c == 'n')
                  {
                     length++;
                  }
                  else
                  {
                     length = 0;
                     state = State::START;
                     --i;
                  }
                  break;
               case 2:
                  if (c == 'e')
                  {
                     if (firstChar == 'a')
                     {
                        firstChar = '1';
                     }
                     else
                     {
                        lastChar = '1';
                     }
                     length = 0;
                     --i;
                     state = State::START;
                  }
                  else
                  {
                     length = 0;
                     state = State::START;
                     i -= 2;
                  }
                  break;
               default:
                  break;
               }
               break;
            case State::T:
               switch (c)
               {
               case 'h':
                  length++;
                  state = State::TH;
                  break;
               case 'w':
                  length++;
                  state = State::TW;
                  break;
               default:
                  length = 0;
                  state = State::START;
                  --i;
                  break;
               }
               break;
            case State::F:
               switch (c)
               {
               case 'o':
                  length++;
                  state = State::FO;
                  break;
               case 'i':
                  length++;
                  state = State::FI;
                  break;
               default:
                  length = 0;
                  state = State::START;
                  --i;
                  break;
               }
               break;
            case State::S:
               switch (c)
               {
               case 'i':
                  length++;
                  state = State::SI;
                  break;
               case 'e':
                  length++;
                  state = State::SE;
                  break;
               default:
                  length = 0;
                  state = State::START;
                  --i;
                  break;
               }
               break;
            case State::E:
               switch (length)
               {
               case 1:
                  if (c == 'i')
                  {
                     ++length;
                  }
                  else
                  {
                     length = 0;
                     --i;
                     state = State::START;
                  }
                  break;
               case 2:
                  if (c == 'g')
                  {
                     ++length;
                  }
                  else
                  {
                     i -= length;
                     length = 0;
                     state = State::START;
                  }
                  break;
               case 3:
                  if (c == 'h')
                  {
                     ++length;
                  }
                  else
                  {
                     i -= length;
                     length = 0;
                     state = State::START;
                  }
                  break;
               case 4:
                  if (c == 't')
                  {
                     length = 0;
                     state = State::START;

                     if (firstChar == 'a')
                     {
                        firstChar = '8';
                     }
                     else
                     {
                        lastChar = '8';
                     }
                     --i;
                  }
                  else
                  {
                     i -= length;
                     length = 0;
                     state = State::START;
                  }
                  break;
               default:
                  break;
               }
               break;
            case State::N:
               switch (length)
               {
               case 1:
                  if (c == 'i')
                  {
                     ++length;
                  }
                  else{
                     i -= length;
                     length = 0;
                     state = State::START;
                  }
                  break;
               case 2:
                  if (c == 'n')
                  {
                     ++length;
                  }
                  else
                  {
                     i -= length;
                     length = 0;
                     state = State::START;
                  }
                  break;
               case 3:
                  if (c == 'e')
                  {
                     length = 0;
                     state = State::START;

                     if (firstChar == 'a')
                     {
                        firstChar = '9';
                     }
                     else
                     {
                        lastChar = '9';
                     }
                     --i;
                  }
                  else
                  {
                     i -= length;
                     length = 0;
                     state = State::START;
                  }
                  break;
               default:
                  break;
               }
               break;
            case State::TH:
               switch (length)
               {
               case 2:
                  if (c == 'r')
                  {
                     ++length;
                  }
                  else
                  {
                     i -= length;
                     length = 0;
                     state = State::START;
                  }
                  break;
               case 3:
                  if (c == 'e')
                  {
                     ++length;
                  }
                  else
                  {
                     i -= length;
                     length = 0;
                     state = State::START;
                  }
                  break;
               case 4:
                  if (c == 'e')
                  {
                     length = 0;
                     state = State::START;

                     if (firstChar == 'a')
                     {
                        firstChar = '3';
                     }
                     else
                     {
                        lastChar = '3';
                     }
                     --i;
                  }
                  else
                  {
                     i -= length;
                     length = 0;
                     state = State::START;
                  }
                  break;
               default:
                  break;
               }
               break;
            case State::TW:
               if (c == 'o')
               {
                  if (firstChar == 'a')
                  {
                     firstChar = '2';
                  }
                  else
                  {
                     lastChar = '2';
                  }
                  --i;
               }
               else
               {
                  i -= length;
               }

               state = State::START;
               length = 0;
               break;
            case State::FO:
               switch (length)
               {
               case 2:
                  if (c == 'u')
                  {
                     ++length;
                  }
                  else
                  {
                     i -= length;
                     length = 0;
                     state = State::START;
                  }
                  break;
               case 3:
                  if (c == 'r')
                  {
                     length = 0;
                     state = State::START;

                     if (firstChar == 'a')
                     {
                        firstChar = '4';
                     }
                     else
                     {
                        lastChar = '4';
                     }
                     --i;
                  }
                  else
                  {
                     i -= length;
                     length = 0;
                     state = State::START;
                  }
                  break;
               default:
                  break;
               }
               break;
            case State::FI:
            switch (length)
            {
            case 2:
               if (c == 'v')
               {
                  ++length;
               }
               else
               {
                  i -= length;
                  length = 0;
                  state = State::START;
               }
               break;
            case 3:
               if (c == 'e')
               {
                  length = 0;
                  state = State::START;

                  if (firstChar == 'a')
                  {
                     firstChar = '5';
                  }
                  else
                  {
                     lastChar = '5';
                  }
                  --i;
               }
               else
               {
                  i -= length;
                  length = 0;
                  state = State::START;
               }
               break;
            default:
               break;
            }
               break;
            case State::SI:
               if (c == 'x')
               {
                  if (firstChar == 'a')
                  {
                     firstChar = '6';
                  }
                  else
                  {
                     lastChar = '6';
                  }
                  --i;
               }
               else
               {
                  i -= length;
               }

               state = State::START;
               length = 0;
               break;
            case State::SE:
               switch (length)
               {
               case 2:
                  if (c == 'v')
                  {
                     ++length;
                  }
                  else
                  {
                     i -= length;
                     length = 0;
                     state = State::START;
                  }
                  break;
               case 3:
                  if (c == 'e')
                  {
                     ++length;
                  }
                  else
                  {
                     i -= length;
                     length = 0;
                     state = State::START;
                  }
                  break;
               case 4:
                  if (c == 'n')
                  {
                     length = 0;
                     state = State::START;

                     if (firstChar == 'a')
                     {
                        firstChar = '7';
                     }
                     else
                     {
                        lastChar = '7';
                     }
                     --i;
                  }
                  else
                  {
                     i -= length;
                     length = 0;
                     state = State::START;
                  }
                  break;
               default:
                  break;
               }
               break;
            default:
               break;
            }
         }

         int k = 0;
      }

      if (lastChar == 'a')
      {
         lastChar = firstChar;
      }

      std::cout << "Line: " << firstChar << lastChar << std::endl;
      
      std::stringstream ss;
      ss << firstChar << lastChar;
      int num;
      ss >> num;
      sum += num;
   }

   std::cout << sum << std::endl;
}
