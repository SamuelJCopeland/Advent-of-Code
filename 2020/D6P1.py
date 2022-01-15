#Advent of Code
#Day 6

groups = []
num_people = 0
answers = open("answers.txt",'r').readlines()
#print(answers)
temp = ""
for a in answers:
    if a == "\n":
        templist = []
        for c in temp:
            if temp.count(c) == num_people:
                templist.append(c)
        
        temp = ""
        num_people = 0
        groups.append(list(dict.fromkeys(templist)))
    else:
        temp = temp + a[:-1]
        num_people = num_people + 1
        
            

templist = []
for c in temp:
    if temp.count(c) == num_people:
        templist.append(c)

temp = ""
num_people = 0
groups.append(list(dict.fromkeys(templist)))

#print(groups)
sum_ = 0
for g in groups:
    sum_ = sum_ + len(g)
print(sum_)