#Advent of Code
#Day 9

def find_weakness(data = [], test_num = 0, begin = 0, end = 1):
    total = 0
    min_ = data[begin]
    max_ = data[begin]
    
    for i in range(begin, end + 1):
        total += data[i]
        if data[i] < min_:
            min_ = data[i]
        if data[i] > max_:
            max_ = data[i]
    if total == test_num:
        print(min_)
        print(max_)
        return min_ + max_
    elif total < test_num:
        return find_weakness(data, test_num, begin, end + 1)
    else:
        return find_weakness(data, test_num, begin + 1, end)

data = open("XMAS.txt",'r').readlines()
prev = []

prev_index = -25
index = 0
    
for i in range(0, 25):
    prev.append(int(data[i][:-1]))
    index += 1
    prev_index += 1

odd_num = 0

for i in range(index, len(data)):
    #Check to see if the next number is a sum of two of the previous 25 numbers
    next_num = int(data[i][:-1])
    found = False
    for j in range(prev_index, prev_index + 25):
        for k in range(prev_index, prev_index + 25):
            if k != j and prev[j] + prev[k] == next_num:
                found = True
                break
        if found:
            break
    prev_index += 1
    if not found:
        print(next_num)
        odd_num = next_num
        break
    else:
        prev.append(next_num)
        
f_data = []
for d in data:
    f_data.append(int(d[:-1]))
print(find_weakness(f_data, odd_num, 0, 1))

