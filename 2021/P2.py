forward = 0
depth = 0
aim = 0
with open("P2.txt", "r") as a_file:

    for line in a_file:

        direction = line.split(" ")[0]
        amount = int(line.split(" ")[1])
        
        if direction == "forward":
            forward += amount
            depth += amount * aim
        elif direction == "backward":
            forward -= amount
            depth -= amount * aim
        elif direction == "down":
            aim += amount
        else:
            aim -= amount
print(forward * depth)