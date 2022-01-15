with open("P7.txt", "r") as file:

    line = file.readline()
    line = line.split(",")
    positions = []
    for n in line:
        positions.append(int(n))
        
    positions.sort()
    last = positions[-1]
    totals = []
    for n in positions:
        if n != last:
            total = 0
            for i in positions:
                total += sum(range(0, abs(i - n) + 1))
            totals.append(total)
            
    totals.sort()
    print(totals[0])
    print(totals[-1])