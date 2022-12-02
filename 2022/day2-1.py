rounds = []
move_map = {'A':'R', 'B':'P', 'C':'S', 'X':'R', 'Y':'P', 'Z':'S'}
point_map = {'R' : 1, 'P' : 2, 'S' : 3}

score = 0

with open(r"2022/input2.txt", "r") as input_file:
    for line in input_file:
        l = move_map[line[0]]
        r = move_map[line[2]]

        score += point_map[r]

        if l == r:
            score += 3
        elif l == 'R' and r == 'P' or l == 'P' and r == 'S' or l == 'S' and r == 'R':
            score += 6
print(score)