forest = []
with open(r"2022/input8.txt", "r") as input_file:
    for line in input_file:
        row = []
        for t in line[:-1]:
            row.append(int(t))
        forest.append(row)
#print(forest)
maxScore = 0
for i in range(1, len(forest) - 1):
    for j in range(1, len(forest[0]) - 1):
        treeHeight = forest[i][j]
        visible = [0, 0, 0, 0]
        #Check visibility from left
        for k in range(j-1, -1, -1):
            visible[0] += 1
            if forest[i][k] >= treeHeight:
                break
        #Check visibility from right
        for k in range(j+1, len(forest[0])):
            visible[1] += 1
            if forest[i][k] >= treeHeight:
                break
        #Check visibility from top
        for k in range(i-1, -1, -1):
            visible[2] += 1
            if forest[k][j] >= treeHeight:
                break
        #Check visibility from bottom
        for k in range(i+1, len(forest)):            
            visible[3] += 1
            if forest[k][j] >= treeHeight:
                break
        score = visible[0] * visible[1] * visible[2] * visible[3]
        if score > maxScore:
            maxScore = score
#NUMBER IS TOO HIGH
print(maxScore)