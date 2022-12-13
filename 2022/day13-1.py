def parseLine(line, arr):
    depth = 0
    l = ''
    i = 1
    while i < len(line):
        c = line[i]
        if depth == 0 and c == '[':
            depth += 1
            newArr = []
            if l != '':
                l = l.split(',')
                res = []
                for n in l:
                    if n != '':
                        arr.append(int(n))
                l = ''
            arr.append(newArr)
            i += parseLine(line[i:], newArr)
            depth -= 1
        elif depth == 0 and c == ']':
            if l != '':
                l = l.split(',')
                res = []
                for n in l:
                    if n != '':
                        arr.append(int(n))
                l = ''
            return i
        elif depth == 0:
            l += c        
        elif depth > 0 and c == ']':
            depth -= 1
        i += 1

def parsePair(l, r):
    for i in range(min(len(l), len(r))):
        sub_valid = 5
        if type(l[i]) != list and type(r[i]) != list:
            if l[i] < r[i]:
                return 1
            elif l[i] > r[i]:
                return 0
        elif type(l[i]) == list and type(r[i]) == list:
            sub_valid = parsePair(l[i], r[i])
        elif type(l[i]) == list and type(r[i]) != list:
            sub_valid = parsePair(l[i], [r[i]])
        else:
            sub_valid = parsePair([l[i]], r[i])
        if sub_valid == 0:
            return 0
        elif sub_valid == 1:
            return 1
    if len(l) < len(r):
        return 1
    elif len(l) == len(r):
        return -1
    else:
        return 0



inputs = []
with open(r"2022/input13.txt", "r") as input_file:
    for line in input_file:
        line = line[:-1]
        if line != '':
            i = []
            parseLine(line, i)
            inputs.append(i)

#Go through inputs 2 at a time, if an entry is a list, enter the list
#Write a recursive function for this
valid_pairs = []
pair = 1
for i in range(0, len(inputs), 2):
    if parsePair(inputs[i], inputs[i+1]) == 1:
        valid_pairs.append(pair)
    pair += 1

print(sum(valid_pairs))