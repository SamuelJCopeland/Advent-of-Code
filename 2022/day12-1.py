class MapLocation:
    def __init__(self, i, j, map):
        self.available_locs = []
        self.val = map[i][j]
        self.dist = 999999999999999999999999999
        if i - 1 > -1:
            other = map[i-1][j]
            if ord(other) - ord(self.val) == 1:
                self.available_locs.append([i-1,j])
            elif ord(self.val) >= ord(other):
                self.available_locs.append([i-1,j])
        if i + 1 < len(map):
            other = map[i+1][j]
            if ord(other) - ord(self.val) == 1:
                self.available_locs.append([i+1,j])
            elif ord(self.val) >= ord(other):
                self.available_locs.append([i+1,j])
        if j - 1 > -1:
            other = map[i][j-1]
            if ord(other) - ord(self.val) == 1:
                self.available_locs.append([i,j-1])
            elif ord(self.val) >= ord(other):
                self.available_locs.append([i,j-1])
        if j + 1 < len(map[i]):
            other = map[i][j+1]
            if ord(other) - ord(self.val) == 1:
                self.available_locs.append([i,j+1])
            elif ord(self.val) >= ord(other):
                self.available_locs.append([i,j+1])

map = []
c_map = []

with open(r"2022/input12.txt", "r") as input_file:
    for line in input_file:
        map.append(line[:-1])

for r in map:
    print(r)

my_pos = [-1,-1]
dest_pos = [-1,-1]
for i in range(len(map)):
    if my_pos[0] > -1 and dest_pos[0] > -1:
        break
    for j in range(len(map[i])):
        if map[i][j] == 'S':
            my_pos = [i,j]
            map[i] = map[i][:j] + 'a' + map[i][j+1:]
        elif map[i][j] == 'E':
            dest_pos = [i,j]
            map[i] = map[i][:j] + 'z' + map[i][j+1:]

for i in range(len(map)):
    temp = []
    for j in range(len(map[i])):
        new_loc = MapLocation(i,j,map)
        temp.append(new_loc)
    c_map.append(temp)

current = c_map[my_pos[0]][my_pos[1]]
    
current.dist = 0

pos_queue = [my_pos]

while len(pos_queue) > 0:
    cur_pos = pos_queue.pop(0)

    current = c_map[cur_pos[0]][cur_pos[1]]

    for p in current.available_locs:
        if c_map[p[0]][p[1]].dist == 999999999999999999999999999:
            c_map[p[0]][p[1]].dist = current.dist + 1
            pos_queue.append(p)



print(c_map[dest_pos[0]][dest_pos[1]].dist)