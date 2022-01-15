class Octopus:
    energy = 0
    flashed = False
    i = 0
    j = 0
    
    def setVals(y, x, e):
        i = y
        j = x
        energy = e

def ocCheck(ocQueue, grid, total):
    #print("checking: " + str(total))
    
    c = 0
    if len(ocQueue) > 0:
        c = ocQueue.pop(0)
    else:
        return total
    i = c.i
    j = c.j
    if c.energy > 9:
    
        total += 1
        c.energy = 0
        c.flashed = True
        #print(str(i) + ", " + str(j))
        if i > 0:
            if j > 0:
                if not grid[i-1][j-1].flashed:
                    #print("y1")
                    grid[i-1][j-1].energy += 1
                    ocQueue.append(grid[i-1][j-1])
            if j < 9:
                if not grid[i-1][j+1].flashed:
                    #print("y2")
                    grid[i-1][j+1].energy += 1
                    ocQueue.append(grid[i-1][j+1])
            if not grid[i-1][j].flashed:
                #print("y3")
                grid[i-1][j].energy += 1
                ocQueue.append(grid[i-1][j])
        if i < 9:
            if j > 0:
                if not grid[i+1][j-1].flashed:
                    #print("y4")
                    grid[i+1][j-1].energy += 1
                    ocQueue.append(grid[i+1][j-1])
            if j < 9:
                if not grid[i+1][j+1].flashed:
                    #print("y5")
                    grid[i+1][j+1].energy += 1
                    ocQueue.append(grid[i+1][j+1])
            if not grid[i+1][j].flashed:
                #print("y6")
                grid[i+1][j].energy += 1
                ocQueue.append(grid[i+1][j])
        if j > 0:
            if not grid[i][j-1].flashed:
                #print("y7")
                grid[i][j-1].energy += 1
                ocQueue.append(grid[i][j-1])
        if j < 9:
            if not grid[i][j+1].flashed:
                #print("y8")
                grid[i][j+1].energy += 1
                ocQueue.append(grid[i][j+1])
    
    return ocCheck(ocQueue, grid, total)
    
grid = []

with open("P11.txt", "r") as file:
    i = 0
    for line in file:
        temp = list(line[:-1])
        l = []
        j = 0
        for a in temp:
            newOc = Octopus()
            newOc.i = i
            newOc.j = j
            newOc.energy = int(a)
            l.append(newOc)
            
            j += 1

        grid.append(l)
        i += 1
total = 0
myQueue = []
i = -1
while True:
    i += 1
    match = grid[0][0].energy + 1
    same = True
    for line in grid:
        for item in line:
            #print(item.energy, end=" ")
            item.flashed = False
            item.energy += 1
            if item.energy != match:
                same = False
            if item.energy > 9:
                myQueue.append(item)
        #print()
    #print(len(myQueue))
    #input()
    #print("Step: " + str(i))
    total += ocCheck(myQueue, grid, 0)
    if same:
        print(i)
        break
print(total)
    