#Advent of Code
#Day 16

def removeNewline(inputString):
    if inputString[-1] == '\n':
        return inputString[:-1]
    else:
        return inputString

pInput = list(map(removeNewline, open("tickets.txt",'r').readlines()))
#print(pInput)
ticket = pInput[22]
otherTickets = pInput[25:]
rules = pInput[0:20]

validVals = {}
solvedFields = {}

for r in rules:
    c = r.split(': ')[0]
    solvedFields[c] = []
    validVals[c] = []
    range1 = r.split(': ')[1].split(' or ')[0]
    range2 = r.split(': ')[1].split(' or ')[1]
    
    for i in range(int(range1.split('-')[0]), int(range1.split('-')[1]) + 1):
        validVals[c].append(i)
    for i in range(int(range2.split('-')[0]), int(range2.split('-')[1]) + 1):
        validVals[c].append(i)
    #print(validVals[c])
    #input()
errorRate = 0
invalidTickets = []
for t in otherTickets:
    validTicket = True
    for n in t.split(','):
        valid = False
        n = int(n)
        for v in validVals:
            if n in validVals[v]:
                valid = True
                break
        if not valid:
            errorRate += n
            validTicket = False
    if not validTicket:
        invalidTickets.append(t)
for t in invalidTickets:
    otherTickets.remove(t)


print(errorRate)

exclude = {}
for i in range(0, len(otherTickets[0].split(','))):
    exclude[i] = []

for t in otherTickets:
    potential = {}
    numbers = list(map(int, t.split(',')))
    for i in range(0, len(numbers)):
        for v in validVals:
            if numbers[i] in validVals[v]:
                if not i in solvedFields[v]:
                    solvedFields[v].append(i)
            else:
                exclude[i].append(v)
        
for s in solvedFields:
    for e in exclude:
        if s in exclude[e]:
            try:
                solvedFields[s].remove(e)
            except:
                continue

solved = False
while not solved:
    count = 0
    for s in solvedFields:
        if len(solvedFields[s]) == 1:
            count += 1
            for t in solvedFields:
                try:
                    if t != s:
                        solvedFields[t].remove(solvedFields[s][0])
                except:
                    continue
            #print(solvedFields)
            #input()
    if count == 20:
        solved = True
print(solvedFields)
finalResult = 1
for s in solvedFields:
    if s.split(' ')[0] == 'departure':
            finalResult *= list(map(int, ticket.split(',')))[solvedFields[s][0]]
print(finalResult)