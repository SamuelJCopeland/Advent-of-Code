#Advent of Code
#Day 10

adaptors = []
for a in open("jolts.txt", 'r').readlines():
    adaptors.append(int(a[:-1]))

adaptors.sort()
jolt3 = 1
jolt1 = 0

if adaptors[0] == 1:
    jolt1 += 1
elif adaptors[0] == 3:
    jolt3 += 1

for i in range(1, len(adaptors)):
    if adaptors[i] - adaptors[i-1] == 1:
        jolt1 += 1
    elif adaptors[i] - adaptors[i-1] == 3:
        jolt3 += 1
#print(jolt1 * jolt3)

arrangements = 1
max_index = 1
min_index = 0
groups = []
adaptors = [0] + adaptors + [adaptors[-1] + 3]
print(adaptors)
temp = []
while max_index < len(adaptors):
    if (adaptors[max_index] - adaptors[min_index]) == 3:
        temp = adaptors[min_index:max_index + 1]
        groups.append(temp)
        min_index = max_index
        max_index = max_index + 1
        temp = []
    elif (adaptors[max_index] - adaptors[min_index]) < 3:
        temp = adaptors[min_index:max_index + 1]
        max_index += 1
    elif (adaptors[max_index] - adaptors[min_index]) > 3:
        groups.append(temp)
        temp = []
        min_index = max_index - 1

for g in groups:
    if len(g) == 3:
        arrangements *= 2
    elif len(g) == 4:
        arrangements *= 4
    elif len(g) > 4:
        print(len(g))
print(arrangements)