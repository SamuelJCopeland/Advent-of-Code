#Advent of Code
#Day #1
#Problem 1

num_file = open("numbers.txt", "r")

lines = num_file.readlines()

for i in range(0, len(lines)):
    lines[i] = lines[i][:-1]
    lines[i] = int(lines[i])

for n1 in lines:
    for n2 in lines:
        for n3 in lines:
            if (n1 != n2) and (n2 != n3) and (n1 != n3) and n1 + n2 + n3 == 2020:
                print(n1*n2*n3)