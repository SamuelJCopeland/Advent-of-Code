overlaps = 0
with open(r"2022/input4.txt", "r") as input_file:
    for line in input_file:
        line = line[:-1].split(",")
        l = line[0].split("-")
        r = line[1].split("-")

        l_l = int(l[0])
        l_r = int(l[1])
        r_l = int(r[0])
        r_r = int(r[1])

        if r_r >= l_r and r_l <= l_r:
            overlaps += 1
        elif l_r >= r_r and l_l <= r_r:
            overlaps += 1
print(overlaps)
