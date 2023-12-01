def checkPocket(i, j, k, min_i, min_j, min_k, max_i, max_j, max_k, coords, visited={}, solved={}):
    visited[f'{i},{j},{k}'] = True
    key = f'{i},{j},{k}'
    if key in solved:
        return solved[key]
    if i <= min_i or i >= max_i or j <= min_j or j >= max_j or k <= min_k or k >= max_k:
        solved[key] = True
        return True

    queue = [[i,j,k]]

    while(len(queue) > 0):
        c = queue.pop(0)
        i = c[0]
        j = c[1]
        k = c[2]

        visited[f'{i},{j},{k}'] = True
        n_key = f'{i},{j},{k}'
        if n_key in solved:
            return solved[n_key]
        if i <= min_i or i >= max_i or j <= min_j or j >= max_j or k <= min_k or k >= max_k:
            solved[n_key] = True
            return True

        if not [i-1,j,k] in coords and not f'{i-1},{j},{k}' in visited:
            if not [i-1, j, k] in queue:
                queue.append([i-1, j, k])
        if not [i+1, j, k] in coords:
            if not [i+1, j, k] in queue:
                queue.append([i+1, j, k])
        if not [i,j-1,k] in coords:
            if not [i, j-1, k] in queue:
                queue.append([i, j-1, k])
        if not [i, j+1, k] in coords:
            if not [i, j+1, k] in queue:
                queue.append([i, j+1, k])
        if not [i,j,k-1] in coords:
            if not [i, j, k-1] in queue:
                queue.append([i, j, k-1])
        if not [i, j,k+1] in coords:
            if not [i, j, k+1] in queue:
                queue.append([i, j, k+1])
    
    solved[key] = False
    return False
    


coords = []
min_i = 9999
max_i = 0
min_j = 9999
max_j = 0
min_k = 9999
max_k = 0
solved = {}
with open(r"2022/input18.txt", "r") as input_file:
    for line in input_file:
        coord = []
        line = line[:-1].split(',')
        coord.append(int(line[0]))
        coord.append(int(line[1]))
        coord.append(int(line[2]))
        coords.append(coord)

        min_i = min(int(line[0]), min_i)
        max_i = max(int(line[0]), max_i)
        min_j = min(int(line[1]), min_j)
        max_j = max(int(line[1]), max_j)
        min_k = min(int(line[2]), min_k)
        max_k = max(int(line[2]), max_k)


# Treat the max and min coordinates as the points of a cube, start on the outside of the cube, and work inward, checking if the sub_cube is air and if so, if it is connected to the outside.
max_c = max(max_i, max_j, max_k)
min_c = min(min_i, min_j, min_k)

while max_c >= min_c:
    print(f'Min: {min_c}\nMax: {max_c}\n')
    # min_c, j, k plane
    for j in range(min_j, max_j + 1):
        for k in range(min_k, max_k + 1):
            key = f'{min_c},{j},{k}'
            #WE NEED TO CHANGE THIS LOGIC
            if not [min_c, j, k] in coords:
                checkPocket(min_c, j, k, min_i, min_j, min_k, max_i, max_j, max_k, coords, visited={}, solved=solved)

    # min_c, i,k plane
    for i in range(min_i, max_i + 1):
        for k in range(min_k, max_k + 1):
            key = f'{i},{min_c},{k}'
            #WE NEED TO CHANGE THIS LOGIC
            if not [i, min_c, k] in coords:
                checkPocket(i, min_c, k, min_i, min_j, min_k, max_i, max_j, max_k, coords, visited={}, solved=solved)

    # min_c, i, j plane
    for i in range(min_i, max_i + 1):
        for j in range(min_j, max_j + 1):
            key = f'{i},{j},{min_c}'
            #WE NEED TO CHANGE THIS LOGIC
            if not [i, j, min_c] in coords:
                checkPocket(i, j, min_c, min_i, min_j, min_k, max_i, max_j, max_k, coords, visited={}, solved=solved)

    # max_c, j, k plane
    for j in range(min_j, max_j + 1):
        for k in range(min_k, max_k + 1):
            key = f'{max_c},{j},{k}'
            #WE NEED TO CHANGE THIS LOGIC
            if not [max_c, j, k] in coords:
                checkPocket(max_c, j, k, min_i, min_j, min_k, max_i, max_j, max_k, coords, visited={}, solved=solved)

    # max_c, i,k plane
    for i in range(min_i, max_i + 1):
        for k in range(min_k, max_k + 1):
            key = f'{i},{max_c},{k}'
            #WE NEED TO CHANGE THIS LOGIC
            if not [i, max_c, k] in coords:
                checkPocket(i, max_c, k, min_i, min_j, min_k, max_i, max_j, max_k, coords, visited={}, solved=solved)

    # max_c, i, j plane
    for i in range(min_i, max_i + 1):
        for j in range(min_j, max_j + 1):
            key = f'{i},{j},{max_c}'
            #WE NEED TO CHANGE THIS LOGIC
            if not [i, j, max_c] in coords:
                checkPocket(i, j, max_c, min_i, min_j, min_k, max_i, max_j, max_k, coords, visited={}, solved=solved)
    max_c -= 1
    min_c += 1

# Go through each coordinate, checking sides one at a time by seeing if there is anything on either side of each point.
# If a side is exposed, add to the total
total_exposed = 0
for c in coords:
    i = c[0]
    j = c[1]
    k = c[2]

    if not [i-1,j,k] in coords:
        if checkPocket(i-1, j, k, min_i, min_j, min_k, max_i, max_j, max_k, coords, visited= {}, solved=solved):
            total_exposed += 1
    if not [i+1, j, k] in coords:
        if checkPocket(i+1, j, k, min_i, min_j, min_k, max_i, max_j, max_k, coords, visited= {}, solved=solved):
            total_exposed += 1
    if not [i,j-1,k] in coords:
        if checkPocket(i, j-1, k, min_i, min_j, min_k, max_i, max_j, max_k, coords, visited= {}, solved=solved):
            total_exposed += 1
    if not [i, j+1, k] in coords:
        if checkPocket(i, j+1, k, min_i, min_j, min_k, max_i, max_j, max_k, coords, visited= {}, solved=solved):
            total_exposed += 1
    if not [i,j,k-1] in coords:
        if checkPocket(i, j, k-1, min_i, min_j, min_k, max_i, max_j, max_k, coords, visited= {}, solved=solved):
            total_exposed += 1
    if not [i, j,k+1] in coords:
        if checkPocket(i, j, k+1, min_i, min_j, min_k, max_i, max_j, max_k, coords, visited= {}, solved=solved):
            total_exposed += 1

print(total_exposed)
