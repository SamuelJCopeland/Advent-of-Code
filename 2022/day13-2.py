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
                #arr.append(res)
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
                #arr.append(res)
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
inputs.append([[2]])
inputs.append([[6]])

n_inputs = []

for i in range(len(inputs)):
    found = False
    for j in range(len(inputs)):
        if j >= len(n_inputs):
            break
        if parsePair(inputs[i], n_inputs[j]) == 1:
            n_inputs.insert(j, inputs[i])
            found = True
            break
    if not found:
        n_inputs.append(inputs[i])
        

key_pos = []
for i in range(len(n_inputs)):
    if n_inputs[i] == [[6]] or n_inputs[i] == [[2]]:
        key_pos.append(i+1)
        if len(key_pos) == 2:
            break
print(key_pos[0] * key_pos[1])