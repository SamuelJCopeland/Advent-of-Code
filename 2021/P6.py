with open("P6.txt", "r") as file:
    line = file.readline()
    line = line.split(",")
    days = [0]*9
    for i in line:
        days[int(i)] += 1
    for i in range(0,256):
        newDays = [0]*9
        newDays[8] += days[0]
        newDays[7] += days[8]
        newDays[6] += days[7] + days[0]
        newDays[5] += days[6]
        newDays[4] += days[5]
        newDays[3] += days[4]
        newDays[2] += days[3]
        newDays[1] += days[2]
        newDays[0] += days[1]
        
        days = newDays
        
    total = 0
    
    for n in days:
        total += n
    print(total)