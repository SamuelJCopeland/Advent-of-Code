coords = []
with open(r"2022/input18.txt", "r") as input_file:
    for line in input_file:
        coord = []
        line = line[:-1].split(',')
        coord.append(int(line[0]))
        coord.append(int(line[1]))
        coord.append(int(line[2]))
        coords.append(coord)

# Go through each coordinate, checking sides one at a time by seeing if there is anything on either side of each point.
# If a side is exposed, add to the total
total_exposed = 0
for c in coords:
    i = c[0]
    j = c[1]
    k = c[2]

    if not [i-1,j,k] in coords:
        total_exposed += 1
    if not [i+1, j, k] in coords:
        total_exposed += 1
    if not [i,j-1,k] in coords:
        total_exposed += 1
    if not [i, j+1, k] in coords:
        total_exposed += 1
    if not [i,j,k-1] in coords:
        total_exposed += 1
    if not [i, j,k+1] in coords:
        total_exposed += 1

print(total_exposed)
