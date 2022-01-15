#Advent of Code
#Day 15

startingNums = open("numberGame.txt",'r').read().split(',')
turnLimit = 30000000
nums = {}
turn = 2
lastNum = startingNums[0]
startingNums = startingNums[1:]
for n in startingNums:
    nums[lastNum] = turn - 1
    lastNum = n
    turn += 1

while turn <= turnLimit:
    if lastNum in nums:
        temp = str(turn - 1 - nums[lastNum])
    else:
        temp = '0'
    nums[lastNum] = turn - 1
    lastNum = temp
    turn += 1
       
print(lastNum)

        
