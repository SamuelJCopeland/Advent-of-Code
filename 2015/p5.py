vowels = {"a", "e", "i", "o", "u"}
not_allowed = {"ab", "cd", "pq", "xy"}
data = []
with open("p5.txt", "r") as input_file:
	data = input_file.readlines()
input_file.close()
#print(data)

num_nice = 0

for l in data:
    nice = True
    for s in not_allowed:
        if s in l:
            nice = False
            break
    num_vowels = 0
    for c in l:
        if c in vowels:
            num_vowels += 1
    if num_vowels < 3:
        nice = False
        continue
    if nice:
        for i in range(0, len(l) - 1):
            if l[i] == l[i+1]:
                num_nice += 1
                break
print(num_nice)

num_nice = 0

for l in data:
    nice = False
    for i in range(0, len(l) - 1):
        if l[i:i+2] in l[i+2:]:
            nice = True
            break
    if nice:
        for i in range(0, len(l) - 2):
            if l[i] == l[i+2]:
                num_nice += 1
                break
print(num_nice)
    
    