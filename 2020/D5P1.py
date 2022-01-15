#Advent of Code
#Day 5
passes = open("passes.txt",'r').readlines()
max_id = 0
num_rows = 128
num_cols = 8
ids = []
for p in passes:
    p = p[:-1]
    begin = 0
    end = num_rows
    for i in range(0, 7):
        if p[i] == 'F':
            end = (end - begin) / 2  + begin
        elif p[i] == 'B':
            begin = (end - begin) / 2 + begin
    row = end - 1
    
    begin = 0
    end = num_cols
    p = p[7:]
    for i in range(0,3):
        print(i)
        if p[i] == 'L':
            end = (end - begin) / 2  + begin
        elif p[i] == 'R':
            begin = (end - begin) / 2 + begin
    col = end - 1        
    
    seat_id = row * 8 + col
    if seat_id > max_id:
        max_id = seat_id
    ids.append(seat_id)
print(max_id)
ids = sorted(ids)
print (ids)
for i in range(0, len(ids)):
    if ids[i+1] - ids[i] == 2:
        print(ids[i+1] - 1)
        break
    