forest = []
with open(r"2022/input8.txt", "r") as input_file:
    for line in input_file:
        row = []
        for t in line[:-1]:
            row.append(int(t))
        forest.append(row)
#print(forest)
numVisible = len(forest)*2 + len(forest[0])*2 - 4
for i in range(1, len(forest) - 1):
    for j in range(1, len(forest[0]) - 1):
        treeHeight = forest[i][j]
        visible = [True, True, True, True]
        #Check visibility from left
        for k in range(0, j):
            if forest[i][k] >= treeHeight:
                visible[0] = False
                break
        #Check visibility from right
        for k in range(len(forest[0])-1, j, -1):
            if forest[i][k] >= treeHeight:
                visible[1] = False
                break
        #Check visibility from top
        for k in range(0, i):
            if forest[k][j] >= treeHeight:
                visible[2] = False
                break
        #Check visibility from bottom
        for k in range(len(forest)-1, i, -1):
            if forest[k][j] >= treeHeight:
                visible[3] = False
                break
        if visible[0] or visible[1] or visible[2] or visible[3]:
            numVisible += 1
#NUMBER IS TOO HIGH
print(numVisible)