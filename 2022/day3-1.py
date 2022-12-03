total = 0
with open(r"2022/input3.txt", "r") as input_file:
    for line in input_file:
        line = line[:-1]
        length = len(line)
        l = line[:length//2]
        r = line[length//2:]
        for c in l:
            if c in r:
                if c.isupper():
                    total += ord(c)-ord('A')+27
                else:
                    total += ord(c)-ord('a')+1
                break

print(total)
