rounds = []
move_map = {'A':'R', 'B':'P', 'C':'S'}
win_map = {'R':'P', 'P':'S', 'S':'R'}
lose_map = {'R':'S', 'P':'R', 'S':'P'}
point_map = {'R' : 1, 'P' : 2, 'S' : 3}

score = 0

with open(r"2022/input2.txt", "r") as input_file:
    for line in input_file:
        l = move_map[line[0]]
        r = line[2]

        if r == 'Y':
            score += 3 + point_map[l]
        elif r == 'Z':
            score += 6 + point_map[win_map[l]]
        else:
            score += point_map[lose_map[l]]

print(score)