import math

def findPath(grid, queue, end, dist, visited={}):
    start = []
    while True:
        minV=dist[queue[0][1]][queue[0][0]]
        minIndex=0
        j=0
        for i in queue:
            x=i[0]
            y=i[1]
            if dist[y][x] < minV and not (str(x) + "," + str(y) + ",") in visited:
                minIndex = j
                minV = dist[y][x]
            j+=1
        start = queue.pop(minIndex)
        testS = ""
        for c in start:
            testS += str(c) + ","
        visited[testS]=0
        result=dijkstra(grid, start, queue, end, dist, visited)
        if result > -1:
            return result
    
def dijkstra(grid, start, queue, end, dist, visited):
    
    
    """
    for l in grid:
        for n in l:
            print(n, end="")
        print()
    print()
    for l in dist:
        for n in l:
            print(n, end=",")
        print()
    
    input()
    """
    testS = ""
    for c in end:
        testS += str(c) + ","
    if testS in visited:
        return dist[end[1]][end[0]]
    x = start[0]
    y = start[1]
    if y > 0:
        if not str(x) + "," + str(y-1) + "," in visited:
            if dist[y][x] + grid[y-1][x] < dist[y-1][x]:
                dist[y-1][x] = dist[y][x] + grid[y-1][x]
            if not [x,y-1] in queue:
                queue.append([x, y-1])
    if y < end[1]:
        if not str(x) + "," + str(y+1) + "," in visited:
            if dist[y][x] + grid[y+1][x] < dist[y+1][x]:
                dist[y+1][x] = dist[y][x] + grid[y+1][x]
            if not [x,y+1] in queue:
                queue.append([x, y+1])
    if x > 0:
        if not str(x-1) + "," + str(y) + "," in visited:
            if dist[y][x] + grid[y][x-1] < dist[y][x-1]:
                dist[y][x-1] = dist[y][x] + grid[y][x-1]
            if not [x-1,y] in queue:
                queue.append([x-1, y])
    if x < end[0]:
        if not str(x+1) + "," + str(y) + "," in visited:
            if dist[y][x] + grid[y][x+1] < dist[y][x+1]:
                dist[y][x+1] = dist[y][x] + grid[y][x+1]
            if not [x-1,y] in queue:
                queue.append([x+1, y])
    return -1
grid = list()
dist = list()
start = list()
end = list()
with open("P15.txt", "r") as file:
    for line in file:
        temp = []
        for c in line[:-1]:
            temp.append(int(c))
        grid.append(temp)
file.close()
start = [0,0]
end = [len(grid[0])-1, len(grid)-1]
for l in grid:
    temp = []
    for i in l:
        temp.append(999999)
    dist.append(temp)
dist[0][0] = 0
#print(findPath(grid, [start], end, dist))
"""
test1=[1,2,3,4]
test2=[5,6,7,8]
test4=[test1, test2,]
test5=[test2, test1]
test3=test1+test2
print(test3)
test6=test4 + test5
print(test6)
print(test6 + test6)
"""
ngrid = [grid]
#make a grid 5 times larger than the previous
#Make 4 grids to the right, then fill in below
for i in range(1,5):
    tempg=[]
    for l in ngrid[i-1]:
        tempr=[]
        for n in l:
            tempr.append((n%9) + 1)
        tempg.append(tempr)
    ngrid.append(tempg)
#Combine the gridrows
fgrid=[]
for j in range(0, len(grid)):
    tempr=[]
    for i in range(0,5):
        tempr+=ngrid[i][j]
    fgrid.append(tempr)
nfgrid=[fgrid]
for i in range(1,5):
    tempg=[]
    for l in nfgrid[i-1]:
        tempr=[]
        for n in l:
            tempr.append((n%9)+1)
        tempg.append(tempr)
    nfgrid.append(tempg)
finalGrid=[]
for g in nfgrid:
    finalGrid+=g
dist=[]    
start = [0,0]
end = [len(finalGrid[0])-1, len(finalGrid)-1]
for l in finalGrid:
    temp = []
    for i in l:
        temp.append(math.inf)
    dist.append(temp)
dist[0][0] = 0
print(findPath(finalGrid, [start], end, dist))

    