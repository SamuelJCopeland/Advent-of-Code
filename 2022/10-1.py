x = 1
cycle = 0
sum = 0
with open(r"2022/input10.txt", "r") as input_file:
    for line in input_file:
        line = line[:-1].split(' ')
        if line[0] == 'addx':
            cycle += 1

            if cycle % 40 == 20:
                sum += cycle*x
            
            cycle += 1

            if cycle % 40 == 20:
                sum += cycle*x
            
            x += int(line[1])
        else:
            cycle += 1
            if cycle % 40 == 20:
                sum += cycle*x
print(sum)