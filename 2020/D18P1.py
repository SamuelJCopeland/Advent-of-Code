#Advent of Code
#Day 18

def removeNewline(inputString):
    if inputString[-1] == '\n':
        return inputString[:-1]
    else:
        return inputString

pInput = list(map(removeNewline, open("cubes.txt",'r').readlines()))

total = 0

