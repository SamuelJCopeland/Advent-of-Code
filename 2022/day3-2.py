total = 0
elves = []
with open(r"2022/input3.txt", "r") as input_file:
    for line in input_file:
        line = line[:-1]
        elves.append(line)
        if len(elves) < 3:
            continue
        for c in elves[0]:
            if c in elves[1] and c in elves[2]:
                if c.isupper():
                    total += ord(c)-ord('A')+27
                else:
                    total += ord(c)-ord('a')+1
                break
        elves = []

print(total)
