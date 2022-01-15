#Advent of Code
#Day 14

instructions = []
maxim = 0
for l in open('docking.txt','r').readlines():
    instructions.append(l[:-1])
    if l[:-1].split(" ")[0][:3] == "mem":
        if int(l[:-1].split(" ")[0].split('[')[1][:-1]) > maxim:
            maxim = int(l[:-1].split(" ")[0].split('[')[1][:-1])
memory = [0] * (maxim + 1) * 2
for i in range(0,len(memory)):
    memory[i] = ['0'] * 36
#print (instructions)
mask = ""
#Part 1
#print(memory)
for i in instructions:
    if i.split(" ")[0] == "mask":
        mask = i.split(' ')[2]
        #print(mask)
        #input()
    else:
        for  j in range(0, 36):
            memory[int(i.split(" ")[0].split('[')[1][:-1])][j] = format(int(i.split(" ")[-1]), "036b")[j]
            if mask[j] != 'X':
                memory[int(i.split(" ")[0].split('[')[1][:-1])][j] = mask[j]
total = 0
for m in memory:
    total += int("".join(m),2)
print(total)
#part 2
memory = {}
#for i in range(0,len(memory)):
#    memory[i] = ['0'] * 36
    
def floatingBits(address = []):
    results = []
    try:
        i = address.index('X')
        address[i] = '0'
        
        #print("zero:\t" + "".join(address))
        temp = []
        for k in address:
            temp.append(k)
        
        results += floatingBits(temp)
        address[i] = '1'
        temp = []
        for k in address:
            temp.append(k)
        #print("one:\t" + "".join(address))
        #input()
        results += floatingBits(temp)
    except:
        return [address]
    return results


for i in instructions:
    if i.split(" ")[0] == "mask":
        mask = i.split(' ')[2]
    else:
        address = list(format(int(i.split(" ")[0].split('[')[1][:-1]), "036b"))
        #print("".join(address))
        for j in range(0, 36):
            if mask[j] != '0':
                address[j] = mask[j]
        #print("".join(address))
        #input()
        #print(floatingBits(address))
        for a in floatingBits(address):
            #print("".join(a))
            a = int("".join(a),2)
            memory[a] = list(format(int(i.split(" ")[-1]), "036b"))
        #input()
total = 0
for m in memory:
    total += int("".join(memory[m]),2)
print(total)