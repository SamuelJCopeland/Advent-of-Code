min_x = 9999999999
max_x = 0
min_y = 9999999999
max_y = 0
map = {}
beacon_dist = {}
with open(r"2022/input15.txt", "r") as input_file:
    for line in input_file:
        line = line[:-1].split(' ')
        s_x = line[2].split('=')[1][:-1]
        s_y = line[3].split('=')[1][:-1]
        
        min_x = min(min_x, int(s_x))
        max_x = max(max_x, int(s_x))
        min_y = min(min_y, int(s_y))
        max_y = max(max_y, int(s_y))

        b_x = line[8].split('=')[1][:-1]
        b_y = line[9].split('=')[1]
        
        min_x = min(min_x, int(b_x))
        max_x = max(max_x, int(b_x))
        min_y = min(min_y, int(b_y))
        max_y = max(max_y, int(b_y))

        map[s_x+','+s_y] = 'S'
        map[b_x+','+b_y] = 'B'

        beacon_dist[s_x+','+s_y] = max(int(s_x), int(b_x)) - min(int(s_x), int(b_x)) + max(int(s_y), int(b_y)) - min(int(s_y), int(b_y))

print(f'Min X: {min_x}, Min Y: {min_y}')
print(f'Max X: {max_x}, Max Y: {max_y}')
print()
"""
for i in range(min_y, max_y + 1):
    row = ''
    for j in range(min_x, max_x+1):
        key = f'{j},{i}'
        if key in map:
            row += map[key]
        else:
            row += '.'
    print(row)
"""

# Add '#'s to represent the Manhatten distances of all of the sensor ranges for their closest beacons
for k in beacon_dist:
    dist = beacon_dist[k]
    k = k.split(',')
    s_x = int(k[0])
    s_y = int(k[1])

    #Go up, decreasing the number covered each time on right and left side
    for i in range(s_y, s_y - dist-1, -1):
        if i < min_y:
            min_y = i
        
        if i != 2000000:
            continue

        for j in range(s_x-1, s_x - dist - 1+s_y-i, -1):
            if j < min_x:
                min_x = j
            
            new_k = f'{j},{i}'
            if not new_k in map:
                map[new_k] = '#'
        #Do the same thing going to the right, except we need to also cover the middle part this time
        for j in range(s_x, s_x + dist + 1 - s_y+i, 1):
            if j > max_x:
                max_x = j
            
            new_k = f'{j},{i}'
            if not new_k in map:
                map[new_k] = '#'
        
    
    #Go down, doing the same thing
    for i in range(s_y, s_y + dist+1):
        if i > max_y:
            max_y = i
        if i != 2000000:
            continue

        for j in range(s_x-1, s_x - dist - 1+i-s_y, -1):
            if j < min_x:
                min_x = j
            
            new_k = f'{j},{i}'
            if not new_k in map:
                map[new_k] = '#'
        #Do the same thing going to the right, except wee need to also cover the middle part this time
        for j in range(s_x, s_x + dist + 1 - i+s_y, 1):
            if j > max_x:
                max_x = j
            
            new_k = f'{j},{i}'
            if not new_k in map:
                map[new_k] = '#'

sum = 0

for j in range(min_x, max_x+1):
    key = f'{j},{2000000}'
    if key in map:
        symbol = map[key]
        if symbol == '#':
            sum += 1
print(sum)


