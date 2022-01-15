#Advent of Code
#Day 8

code = open("code.txt",'r').readlines()
executed = []

for c in code:
    c = c[:-1]

acc = 0
i = 0
prev_i = ""
while i < len(code):
    #print(code[i])
    #print(i)
    #print(acc)
    #input()
    
    if not i in executed:
        executed.append(i)
        prev_i = str(i) + ":\t" + code[i]
        if code[i].split(' ')[0] == 'acc':
            acc = acc + int(code[i].split(' ')[1])
            i = i + 1
        elif code[i].split(' ')[0] == 'jmp':
            if code[i].split(' ')[1][0] == '-':
                i = i - int(code[i].split(' ')[1][1:])
            else:
                i = i + int(code[i].split(' ')[1][1:])
        else:
            i = i + 1
    else:
        print(prev_i)
        print(str(i) + ":\t" + code[i])
        print(executed[-10:])
        break;
        #print(prev_i + 1)
        #print(i)
        #break
    #i = i + 1
print(acc)