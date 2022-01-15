lines = []

with open("p1.txt", "r") as a_file:

   for line in a_file:

    lines.append(int(line))
   
previous = lines[0] + lines[1] + lines[2]
count = 0



for i in range(2, len(lines)):
    
    cSum = lines[i] + lines[i-1] + lines[i-2]
    
    if cSum > previous :
        count+= 1
    previous = cSum
        
print(count)