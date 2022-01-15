def recursiveSolve(inputLine, pairDict, countDict, solved, numTimes):
    for i in range(0, len(inputLine) - 1):
        iterativeSolve(inputLine[i:i+2], pairDict, countDict, solved, numTimes)
    
   
def iterativeSolve(inp, pairDict, countDict, solved, numTimes):
    inputLine = inp
    
    for k in range(0, numTimes):
        if inputLine in solved:
            inputLine = solved[inputLine]
        else:
            newLine = inputLine[0]
            for i in range(0, len(inputLine) - 1):
                insertChar = pairDict[inputLine[i:i+2]]
                newLine += insertChar + inputLine[i+1]
            
            solved[inputLine] = newLine
            inputLine = newLine
    for i in range(1, len(inputLine) - 1):
        if inputLine[i] in countDict:
            countDict[inputLine[i]] += 1
        else:
            countDict[inputLine[i]] = 1
    
def recCount(p, o, pairDict, count, numTimes, solved=[{}], iterator=0):
    #print(p)
    
    if iterator < numTimes:
        if iterator < len(solved):
            if p in solved[numTimes - iterator]:
                for e in solved[numTimes - iterator][p]:
                    if e in count:
                        count[e] += solved[numTimes - iterator][p][e]
                    else:
                        count[e] = solved[numTimes - iterator][p][e]
                #input(count)
                
                return
                
        newC = pairDict[p]
        if newC in count:
            count[newC] += 1
        else:
            count[newC] = 1
        
        
        iterator += 1
        nCount1 = {}
        nCount2 = {}
        recCount(p[0] + newC, o, pairDict, nCount1, numTimes, solved, iterator)
        recCount(newC + p[1], o, pairDict, nCount2, numTimes, solved, iterator)
        
        nCount = {}
        if not o in solved[iterator]:
            solved[iterator][o] = {}
        for e in nCount1:
            if e in solved[iterator][o]:
                solved[iterator][o][e] += nCount1[e]
            else:
                solved[iterator][o][e] = nCount1[e]
            if e in count:
                count[e] += nCount1[e]
            else:
                count[e] = nCount1[e]
        for e in nCount2:
            if e in solved[iterator][o]:
                solved[iterator][o][e] += nCount2[e]
            else:
                solved[iterator][o][e] = nCount2[e]
            if e in count:
                count[e] += nCount2[e]
            else:
                count[e] = nCount2[e]
    print(count)
            
inputLine = ""
pairDict = {}
countDict = {}

with open("P14.txt", "r") as file:
    inputLine = file.readline()[:-1]
    file.readline()
    
    for line in file:
        pairDict[line.split(" -> ")[0]] = line.split(" -> ")[1][:-1]
solved = {}

for e in pairDict:
    solved[e] = e[0] + pairDict[e] + e[1]

for c in inputLine:
    if not c in countDict:
        countDict[c] = 1
    else:
        countDict[c] += 1
pairTotals = {}
s = []
for i in range(0, 40):
    s.append({})

for e in pairDict:
    print(e)
    pairTotals[e] = {}
    recCount(e, e, pairDict, pairTotals[e], 10, s)
    #input(pairTotals[e])


#recursiveSolve(inputLine, pairDict, countDict, solved, 40)

for i in range(0, len(inputLine) - 1):
    for e in pairTotals[inputLine[i:i+2]]:
        if e in countDict:
            #print(pairTotals[inputLine[i:i+2]][e])
            countDict[e] += pairTotals[inputLine[i:i+2]][e]
        else:
            countDict[e] = pairTotals[inputLine[i:i+2]][e]
print(countDict)
maxNum = countDict[inputLine[0]]
minNum  = countDict[inputLine[0]]
for i in countDict:
    if countDict[i] < minNum:
        minNum = countDict[i]
    elif countDict[i] > maxNum:
        maxNum = countDict[i]
print(maxNum - minNum)
