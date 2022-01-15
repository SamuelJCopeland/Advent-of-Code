data = []
grid = []
for i in range(0,1000):
    temp=[]
    for j in range(0,1000):
        temp.append(False)
    grid.append(temp)
with open("p6.txt", "r") as input_file:
	data = input_file.readlines()
input_file.close()
#print(grid)
for i in range(0, len(data)):
    l = data[i]
    if l.split(" ")[0] == "turn":
        data[i] = l[5:]
for l in data:
    instructions = l.split(" ")
    command = instructions[0]
    start = instructions[1]
    end = instructions[3]
    
    if command == "on":
        for i in range(int(start.split(",")[0]), int(end.split(",")[0]) + 1):
            for j in range(int(start.split(",")[1]), int(end.split(",")[1]) + 1):
                grid[i][j] = True
    elif command == "off":
        for i in range(int(start.split(",")[0]), int(end.split(",")[0]) + 1):
            for j in range(int(start.split(",")[1]), int(end.split(",")[1]) + 1):
                grid[i][j] = False
    elif command == "toggle":
        for i in range(int(start.split(",")[0]), int(end.split(",")[0]) + 1):
            for j in range(int(start.split(",")[1]), int(end.split(",")[1]) + 1):
                grid[i][j] = not grid[i][j]
total = 0
for r in grid:
    for i in r:
        if i == True:
            total += 1
print(total)

grid = []
for i in range(0,1000):
    temp=[]
    for j in range(0,1000):
        temp.append(0)
    grid.append(temp)
with open("p6.txt", "r") as input_file:
	data = input_file.readlines()
input_file.close()
#print(grid)
for i in range(0, len(data)):
    l = data[i]
    if l.split(" ")[0] == "turn":
        data[i] = l[5:]
for l in data:
    instructions = l.split(" ")
    command = instructions[0]
    start = instructions[1]
    end = instructions[3]
    
    if command == "on":
        for i in range(int(start.split(",")[0]), int(end.split(",")[0]) + 1):
            for j in range(int(start.split(",")[1]), int(end.split(",")[1]) + 1):
                grid[i][j] += 1
    elif command == "off":
        for i in range(int(start.split(",")[0]), int(end.split(",")[0]) + 1):
            for j in range(int(start.split(",")[1]), int(end.split(",")[1]) + 1):
                if grid[i][j] > 0:
                    grid[i][j] -= 1
    elif command == "toggle":
        for i in range(int(start.split(",")[0]), int(end.split(",")[0]) + 1):
            for j in range(int(start.split(",")[1]), int(end.split(",")[1]) + 1):
                grid[i][j] += 2
total = 0
for r in grid:
    for i in r:
        total += i
print(total)