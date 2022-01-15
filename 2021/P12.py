single = ""
def countPaths(start, upper, lower, visited=[], single={}, myPath="", paths={}):
    #print("visited: " + str(visited))
    #print(single)
    total = 0
    myPath += start + ", "
    
    adjacent = {}
    if start in upper:
        adjacent = upper
    else:
        adjacent = lower
    
    if start[0].islower():
        if start in single:
            single[start] += 1
            if single[start] >= 2:
                visited.append(start)
        else:
            visited.append(start)
        
    
    for n in adjacent[start]:
        #print(adjacent[start])
        if n == "end":
            #input(start + ": " + n)
            #input(myPath + "end")
            if not myPath in paths:
                paths[myPath] = 0
                total += 1
        else:
            if not n in visited:
                #input(start + ": " + n)
                total += countPaths(n, upper, lower, visited, single, myPath, paths)
                if len(single) == 0 and n[0].islower():
                    single[n] = 0
                    total += countPaths(n, upper, lower, visited, single, myPath, paths)
                #print(total)
    if start in visited:
        visited.remove(start)
    if start in single:
        if single[start] >= 2:
            single[start] = 1
        else:
            del(single[start])
    return total
upper = {}
lower = {}
with open("P12.txt", "r") as file:
    for line in file:
        l = line[:-1].split("-")
        if l[0][0].isupper():
            if l[0] in upper:
                upper[l[0]].append(l[1])
            else:
                upper[l[0]] = [l[1]]
        else:
            if l[0] in lower:
                lower[l[0]].append(l[1])
            else:
                lower[l[0]] = [l[1]]
        
        if l[1][0].isupper():
            if l[1] in upper:
                upper[l[1]].append(l[0])
            else:
                upper[l[1]] = [l[0]]
        else:
            if l[1] in lower:
                lower[l[1]].append(l[0])
            else:
                lower[l[1]] = [l[0]]
#print(lower)
print(countPaths("start", upper, lower))