with open(r"2022/input6.txt", "r") as input_file:
    for line in input_file:
        prefix = ''
        for i in range(len(line)):
            prefix += line[i]
            x = prefix[:-1].find(line[i])
            if x > -1:
                prefix = prefix[x+1:]
            elif len(prefix) == 14:
                print(i+1)
                break;
