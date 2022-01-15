with open("P8.txt", "r") as file:
    outputValues = []
    patterns = []
    for line in file:
        outputValues.append(line.split(" | ")[1].split())
        patterns.append(line.split(" | ")[0].split())
    total = 0
    finalSum = 0
    
    for val in outputValues:
        for d in val:
            
            if len(d) == 2:
                total += 1
            elif len(d) == 3:
                total += 1
            elif len(d) == 4:
                total += 1
            elif len(d) == 7:
                total += 1
    index = 0    
    for val in patterns:        
        numMap = {}
        possible = {"a":[], "b":[], "c":[], "d":[], "e":[], "f":[], "g":[]}
        positions = {"a":"a", "b":"b", "c":"c", "d":"d", "e":"e", "f":"f", "g":"g"}
        for d in val:
            if len(d) == 2:
                numMap[1] = d
            elif len(d) == 3:
                numMap[7] = d
            elif len(d) == 4:
                numMap[4] = d
            elif len(d) == 7:
                numMap[8] = d
        for c in numMap[7]:
            if not (c in numMap[1]):
                positions["a"] = c
                break
        count = 0
        for d in val:
            if len(d) == 5:
                for c in d:
                    if not (c in numMap[4]) and not (c in numMap[7]):
                        if not (c in possible["e"]):
                            possible["e"].append(c)
                        if not (c in possible["g"]):
                            possible["g"].append(c)
                count += 1
                if count == 3:
                    break
        #After this we will have 1, 4, 7, 8, 9
        #Still need 0, 2, 3, 5, 6
        for d in val:
            if len(d) == 6:
                for c in possible["e"]:
                    if not (c in d):
                        positions["e"] = c
                        numMap[9] = d
                        possible["g"].remove(c)
                        positions["g"] = possible["g"][0]
                        break
                    
        
        for d in val:
            if len(d) == 5:
                test = True
                for c in numMap[1]:
                    if not (c in d):
                        test = False
                if test:
                    numMap[3] = d
                    for c in d:
                        if not (c in numMap[1]) and c != positions["g"] and c != positions["a"]:
                            positions["d"] = c
                            break
                
        #at this point we know 1, 3, 4, 7, 8, 9
        #We still need to know 0, 2, 5, 6
        #We still need to know b, c, f
        for c in numMap[9]:
            if not (c in numMap[3]):
                positions["b"] = c
                break
        #still need c and f
        for d in val:
            if len(d) == 6 and d != numMap[9]:
                if positions["d"] in d:
                    numMap[6] = d
                else:
                    numMap[0] = d
        #We now have 0, 1, 3, 4, 6, 7, 8, 9
        #We still need to know 2, and 5
        #We know a, b, d, e, and g
        for d in val:
            if len(d) == 5 and d != numMap[3]:
                if positions["b"] in d:
                    numMap[5] = d
                else:
                    numMap[2] = d
        #We now have them all, translate the number
        outputVal = ""
        for d in outputValues[index]:
            for n, s in numMap.items():
                if sorted(s) == sorted(d):
                    outputVal += str(n)
                    break
        finalSum += int(outputVal)
        
        
        index += 1
    #print(total)
    print(finalSum)
    
    
    
