rocks = []
with open(r"2022/input14.txt", "r") as input_file:
    for line in input_file:
        line = line[:-1].split(' -> ')

        for i in range(len(line)-1):
            pair = []
            pair.append([eval(j) for j in line[i].split(',')])
            pair.append([eval(j) for j in line[i+1].split(',')])
            rocks.append(pair)
print(rocks)

# Find min and max x and y
min_x = rocks[0][0][0]
max_x = min_x
min_y = rocks[0][0][1]
max_y = min_y

for pair in rocks:
    for coord in pair:
        x = coord[0]
        y = coord[1]
        if x < min_x:
            min_x = x
        elif x > max_x:
            max_x = x
        
        if y < min_y:
            min_y = y
        elif y > max_y:
            max_y = y
width = max_x - min_x + 1
height = max_y+3
print(f'min_x: {min_x}, max_x: {max_x}, width: {width}\nmin_y: {min_y}, max_y: {max_y}, height: {height}')
print()

# Create a visual representation
map = []
for i in range(height):
    map.append(['.',]*width)

for pair in rocks:
    x_0 = pair[0][0]-min_x
    x_1 = pair[1][0]-min_x
    y_0 = pair[0][1]
    y_1 = pair[1][1]

    x0 = min(x_0, x_1)
    x1 = max(x_0, x_1)
    y0 = min(y_0, y_1)
    y1 = max(y_0, y_1)

    for i in range(y0, y1+1):
        for j in range(x0, x1+1):
            map[i][j] = '#'

for i in range(len(map[height-1])):
    map[height-1][i] = '#'

for row in map:
    temp = ''
    for c in row:
        temp += c
    print(temp)
print()

start = 500 - min_x

sand_pos = [0,start]
prev = [-1, -1]

grains = 0

while(True):
    if map[sand_pos[0]][sand_pos[1]] == '.':
        map[sand_pos[0]][sand_pos[1]] = 'O'
        if prev[0] != -1:
            map[prev[0]][prev[1]] = '.'
        prev[0] = sand_pos[0]
        prev[1] = sand_pos[1]
        sand_pos[0] += 1
    elif sand_pos[1] - 1 > -1 and map[sand_pos[0]][sand_pos[1]-1] == '.':
        map[sand_pos[0]][sand_pos[1]-1] = 'O'
        if prev[0] != -1:
            map[prev[0]][prev[1]] = '.'
        prev[0] = sand_pos[0]
        prev[1] = sand_pos[1]-1
        sand_pos[0] += 1
        sand_pos[1] -= 1
    elif sand_pos[1] + 1 < width and map[sand_pos[0]][sand_pos[1]+1] == '.':
        map[sand_pos[0]][sand_pos[1]+1] = 'O'
        if prev[0] != -1:
            map[prev[0]][prev[1]] = '.'
        prev[0] = sand_pos[0]
        prev[1] = sand_pos[1]+1
        sand_pos[0] += 1
        sand_pos[1] += 1
    elif sand_pos[1] - 1 <= -1:
        for i in range(len(map)):
            if i < len(map)-1:
                map[i].insert(0, '.')
            else:
                map[i].insert(0, '#')
        prev[1] += 1
        sand_pos[1] += 1
        start += 1
        width += 1

    elif sand_pos[1] + 1 >= width:
        for i in range(len(map)):
            if i < len(map)-1:
                map[i].append('.')
            else:
                map[i].append('#')
        width += 1
    else:        
        grains += 1
        if sand_pos[0] - 1 == 0 and sand_pos[1] == start:
            break
        prev = [-1,-1]
        sand_pos = [0, start]

for row in map:
    temp = ''
    for c in row:
        temp += c
    print(temp)
print()
print(grains)