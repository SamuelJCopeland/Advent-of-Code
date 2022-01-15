data = ""
with open("p1.txt", "r") as input_file:
	data = input_file.readline()
input_file.close()
floor = 0
position = 1
printed = False
for c in data:
    if c == "(":
        floor += 1
    elif c == ")":
        floor -= 1
        if floor == -1 and not printed:
            print(position)
            printed = True
    position += 1
print(floor)