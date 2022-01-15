points = {")":3, ']':57, '}':1197, '>':25137}
cPoints = {")":1, ']':2, '}':3, '>':4}
badChars = []
lines = []
with open("P10.txt", "r") as file:
    
    for line in file:
        bad = False
        parStack = []
        for c in line[:-1]:
            if c == '(' or c == '[' or c == '{' or c == '<':
                parStack.append(c)
            elif c == ')':
                if parStack.pop() != '(':
                    badChars.append(c)
                    bad = True
                    break
            elif c == ']':
                if parStack.pop() != '[':
                    badChars.append(c)
                    bad = True
                    break
            elif c == '}':
                if parStack.pop() != '{':
                    badChars.append(c)
                    bad = True
                    break
            elif c == '>':
                if parStack.pop() != '<':
                    badChars.append(c)
                    bad = True
                    break
        if not bad:
            lines.append(line[:-1])
total = 0
for c in badChars:
    total += points[c]
print(total)

total = 0

#print(lines)
#print(parStack)
scores = []
for l in lines:
    total = 0
    parStack = []
    for c in l:
        if c == '(' or c == '[' or c == '{' or c == '<':
            parStack.append(c)
        else:
            parStack.pop()
        #print(c)
        #input(parStack)
    #print(parStack)    
    while len(parStack) > 0:
        c = parStack.pop()
        #print(c)
        if c == '(':
            total *= 5
            total += cPoints[')']
        elif c == '[':
            total *= 5
            total += cPoints[']']
        elif c == '{':
            total *= 5
            total += cPoints['}']
        elif c == '<':
            total *= 5
            total += cPoints['>']
    #input(total)
    scores.append(total)
scores.sort()
print(scores[int(len(scores)/2)])