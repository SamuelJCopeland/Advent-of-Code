elves = []
cals = 0
with open(r"2022/input1.txt", "r") as input_file:
    for line in input_file:
        #print(line)
        if line == "\n":
            elves.append(cals)
            #print(f"cals: {cals}")
            cals = 0
        else:
            cals += int(line)
elves.append(cals) 
elves.sort(reverse=True)
print(elves[0] + elves[1] + elves[2])