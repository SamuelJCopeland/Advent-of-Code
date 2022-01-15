grid = []
for i in range(0, 1000):
    temp = [0]*1000
    grid.append(temp)
with open("P5.txt", "r") as file:
	
    for l in file:
        line = l.split(" -> ")
        c1 = line[0]
        c2 = line[1]
        x1 = int(c1.split(",")[0])
        y1 = int(c1.split(",")[1])
        x2 = int(c2.split(",")[0])
        y2 = int(c2.split(",")[1])
        
        if x1 == x2:
            if y2 > y1:
                for i in range(y1, y2 + 1):
                    grid[i][x1] += 1
            else:
                for i in range(y2, y1 + 1):
                    grid[i][x1] += 1
        elif y1 == y2:
            if x2 > x1:
                for i in range(x1, x2 + 1):
                    grid[y1][i] += 1
            else:
                for i in range(x2, x1 + 1):
                    grid[y1][i] += 1
        elif x1 < x2:
            #down and to the right
            if y1 < y2:
                j = x1
                for i in range(y1, y2 + 1):
                    grid[i][j] += 1
                    j += 1
            
            #up and to the right
            else:
                j = x1
                for i in range(y1, y2 - 1, -1):
                    grid[i][j] += 1
                    j += 1
        else:
            #down and to the left
            if y1 < y2:
                j = x1
                for i in range(y1, y2 + 1):
                    grid[i][j] += 1
                    j -= 1
            
            #up and to the left
            else:
                j = x1
                for i in range(y1, y2 - 1, -1):
                    grid[i][j] += 1
                    j -= 1
    total = 0
    for y in grid:
        #print(y)
        for x in y:
            if x > 1:
                total += 1
                
    print(total)
    
