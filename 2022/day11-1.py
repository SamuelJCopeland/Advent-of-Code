lines = []
with open(r"2022/input11.txt", "r") as input_file:
    for line in input_file:
        lines.append(line[:-1])

#monkeys[0] = [[64, 89, 65, 95], '*', '7', 4, 1, 0]
#The '7' in the above example could also be 'old'
#The last number is a counter to determine how many total items a monkey inspects 
monkeys = []
i = 0
while i < len(lines):
    monkeys.append([])
    i+=1
    #Items the monkey is holding
    items = lines[i].split(': ')[1].split(', ')
    items = [eval(i) for i in items]    
    monkeys[-1].append(items)

    i+=1
    #Worry level increase when the monkey begins inspection
    l = lines[i].split(' ')
    monkeys[-1].append(l[-2])
    monkeys[-1].append(l[-1])

    i+=1
    #Test by monkey
    monkeys[-1].append(int(lines[i].split(" ")[-1]))
    
    i+=1
    #If true
    monkeys[-1].append(int(lines[i][-1]))

    i+=1
    #If false
    monkeys[-1].append(int(lines[i][-1]))
    i+= 2
    monkeys[-1].append(0)


#print(monkeys)
round = 0
while round < 20:
    round += 1
    for monkey in monkeys:
        while len(monkey[0]) > 0:
            item = monkey[0][0]
            monkey[6] += 1

            newVal = 0
            if monkey[1] == '*':
                if monkey[2] == 'old':
                    newVal = item * item
                else:
                    newVal = item * int(monkey[2])
            else:
                if monkey[2] == 'old':
                    newVal = item + item
                else:
                    newVal = item + int(monkey[2])
            newVal = newVal // 3

            test = newVal % monkey[3]
            if test == 0:
                monkeys[monkey[4]][0].append(newVal)
            else:
                monkeys[monkey[5]][0].append(newVal)
            
            monkey[0].pop(0)
numTimes = []
for m in monkeys:
    numTimes.append(m[6])

numTimes.sort(reverse=True)
print(numTimes[0] * numTimes[1])

    