def getBasinSize(i, j, grid, checked):
    size = 1
    if [i,j] in checked:
        return 0
    current = grid[i][j]
    #input(str(current) + ": " + str(i) + ", " + str(j))
    if i > 0:
        if grid[i-1][j] > current and grid[i-1][j] != 9:
            size += getBasinSize(i-1, j, grid, checked)
    if i + 1 < len(grid):
        if grid[i+1][j] > current and grid[i+1][j] != 9:
            size += getBasinSize(i+1, j, grid, checked)
    if j > 0:
        if grid[i][j-1] > current and grid[i][j-1] != 9:
            size += getBasinSize(i, j-1, grid, checked)
    if j + 1 < len(grid[i]):
        if grid[i][j+1] > current and grid[i][j+1] != 9:
            size += getBasinSize(i, j+1, grid, checked)
    #print("size: " + str(size))
    checked.append([i,j])
    return size

with open("P9.txt", "r") as file:
    grid = []
    for line in file:
        l = list(line[:-1])
        temp = []
        for i in l:
            temp.append(int(i))
        grid.append(temp)
    
    total = 0
    basins = []
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            least = True
            if i - 1 >= 0:
                if grid[i-1][j] <= grid[i][j]:
                    least = False
            if i + 1 < len(grid):
                if grid[i+1][j] <= grid[i][j]:
                    least = False
            if j - 1 >= 0:
                if grid[i][j-1] <= grid[i][j]:
                    least = False
            if j + 1 < len(grid[i]):
                if grid[i][j+1] <= grid[i][j]:
                    least = False
            if least:
                total += 1 + grid[i][j]
                #Find the basin size
                basins.append(getBasinSize(i, j, grid, []))
    print(total)
    basins = sorted(basins, reverse=True)
    #print(basins)
    print(basins[0] * basins[1] * basins[2])