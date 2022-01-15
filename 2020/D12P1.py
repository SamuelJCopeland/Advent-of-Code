#Advent of Code
#Day 12

directions = open("directions.txt",'r').readlines()
units_n = 0
units_e = 0
w_n = 1
w_e = 10
#North: 1
#West:  2
#South: 3
#East:  0
facing = 0
for d in  directions:
    #print(facing)
    #print(units_n)
    #print(units_e)
    #print(d[:-1])
    #input()
    d = d[:-1]
    instruction = d[0]
    amount = int(d[1:])
    if instruction == "N":
        w_n += amount
    elif instruction == "S":
        w_n -= amount
    elif instruction == "E":
        w_e += amount
    elif instruction == "W":
        w_e -= amount
    elif instruction == "L":
        prev_dir = facing
        facing += int(amount / 90)
        if facing > 3:
            facing -= 4
        if (amount / 90) % 2 == 0:
            w_n *= -1
            w_e *= -1
        elif amount / 90 == 1:
            temp = w_n
            w_n = w_e
            w_e = temp * -1
        elif amount / 90 == 3:
            temp = w_n
            w_n = w_e
            w_e = temp * -1
            temp = w_n
            w_n = w_e
            w_e = temp * -1
            temp = w_n
            w_n = w_e
            w_e = temp * -1
            
    elif instruction == "R":
        facing -= int(amount / 90)
        if facing < 0:
            facing += 4
            
        if (amount / 90) % 2 == 0:
            w_n *= -1
            w_e *= -1
        elif amount / 90 == 1:
            temp = w_n
            w_n = -1 * w_e
            w_e = temp
        elif amount / 90 == 3:
            temp = w_n
            w_n = -1 * w_e
            w_e = temp
            temp = w_n
            w_n = -1 * w_e
            w_e = temp
            temp = w_n
            w_n = -1 * w_e
            w_e = temp
    elif instruction == "F":
        units_n += w_n * amount
        units_e += w_e * amount
if units_n < 0:
    units_n *= -1
if units_e < 0:
    units_e *= -1
print(units_n + units_e)