dots = []
folds = []
with open("P13.txt", "r") as file:
    foldTime = False
    for line in file:
        if not foldTime:
            if line == "\n":
                foldTime = True
                continue
            else:
                temp = []
                temp.append(int(line.split(',')[0]))
                temp.append(int(line.split(',')[1]))
                dots.append(temp)
        else:
            folds.append(line.split()[2])
grid = []
maxX = 0
maxY = 0
for d in dots:
    if d[0] > maxX:
        maxX = d[0]
    if d[1] > maxY:
        maxY = d[1]
for i in range(0, maxY + 1):
    row = []
    for j in range(0, maxX + 1):
        row.append(0)
    grid.append(row)
for d in dots:
    grid[d[1]][d[0]] = 1

for l in folds:
    splitLine = int(l.split('=')[1])
    if l.split("=")[0] == 'x':
        index = 0
        for d in dots:
            diff = splitLine - d[0]
            dist = abs(diff)
            grid[d[1]][splitLine - dist] = 1
            if diff < 0:
                grid[d[1]][d[0]] = 0
                dots[index] = [splitLine - dist, d[1]]
            index += 1
        
    else:
        index = 0
        for d in dots:
            diff = splitLine - d[1]
            dist = abs(diff)
            grid[splitLine - dist][d[0]] = 1
            if diff < 0:
                grid[d[1]][d[0]] = 0
                dots[index] = [d[0], splitLine - dist]
            index += 1
"""
total = 0

for r in grid:
    for n in r:
        if n == 1:
            total += 1
print(total)
"""
grid = []
maxX = 0
maxY = 0
for d in dots:
    if d[0] > maxX:
        maxX = d[0]
    if d[1] > maxY:
        maxY = d[1]
for i in range(0, maxY + 1):
    row = []
    for j in range(0, maxX + 1):
        row.append(0)
    grid.append(row)
for d in dots:
    grid[d[1]][d[0]] = 1

for r in grid:
    for i in r:
        if i == 0:
            print(".", end="")
        else:
            print("#", end="")
    print()
print(folds)
        