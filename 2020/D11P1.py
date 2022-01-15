#Advent of Code
#Day 11

def check_seats(seats_r = [], xdir = 1, ydir = 1, startx = 0, starty = 0):
    x = startx + xdir
    y = starty + ydir
    if x >= len(seats_r[0]) or x < 0 or y >= len(seats_r) or y < 0:
        return False
    
    if seats_r[y][x] == "#" or seats_r[y][x] == "E":
        return True
    elif seats_r[y][x] == ".":
        return check_seats(seats_r, xdir, ydir, x, y)
    else:
        return False

seat_rows = open('seats.txt', 'r').readlines()
for i in range(0, len(seat_rows)):
    seat_rows[i] = list(seat_rows[i][:-1])
#print(seat_rows)

unchanged = False
time = 0
while not unchanged:
    changed = False
    time = time + 1
    for i in range(0, len(seat_rows)):
        for j in range(0, len(seat_rows[0])):
            #If a seat is empty
            if seat_rows[i][j] == 'L':
                #If there are no occupied seats next to items
                occupied = False
                #Check top 3
                if i > 0:
                    #Top left
                    if j > 0:
                        if check_seats(seat_rows, -1, -1, j, i):
                            occupied = True
                        
                    #Top middle
                    if check_seats(seat_rows, 0, -1, j, i):
                        occupied = True
                    #Top right
                    if j < len(seat_rows[0]) - 1:
                        if check_seats(seat_rows, 1, -1, j, i):
                            occupied = True
                #Check bottom 3
                if i < len(seat_rows) - 1:
                    #bottom left
                    if j > 0:
                        if check_seats(seat_rows, -1, 1, j, i):
                            occupied = True
                        
                    #bottom middle
                    if check_seats(seat_rows, 0, 1, j, i):
                        occupied = True
                    #bottom right
                    if j < len(seat_rows[0]) - 1:
                        if check_seats(seat_rows, 1, 1, j, i):
                            occupied = True
                #Check middle left and right
                if j > 0:
                    if check_seats(seat_rows, -1, 0, j, i):
                        occupied = True
                if j < len(seat_rows[i]) - 1:
                    if check_seats(seat_rows, 1, 0, j, i):
                        occupied = True
                #If all adjacent are unoccupied, then occupy the seat
                if not occupied:
                    seat_rows[i][j] = "X"
                    changed = True
                    #print(seat_rows[i])
                    #input() 
            #If a seat is occupied
            elif seat_rows[i][j] == '#':
                o_count = 0
                #Check top 3
                if i > 0:
                    #Top left and middle left
                    if j > 0:
                        if check_seats(seat_rows, -1, -1, j, i):
                            o_count += 1
                    #Top middle
                    if check_seats(seat_rows, 0, -1, j, i):
                        o_count += 1
                    #Top right and middle right
                    if j < len(seat_rows[0]) - 1:
                        if check_seats(seat_rows, 1, -1, j, i):
                            o_count += 1
                #Check bottom 3
                if i < len(seat_rows) - 1:
                    #bottom left
                    if j > 0:
                        if check_seats(seat_rows, -1, 1, j, i):
                            o_count += 1
                    
                    #bottom middle
                    if check_seats(seat_rows, 0, 1, j, i):
                        o_count += 1
                    #bottom right
                    if j < len(seat_rows[0]) - 1:
                        if check_seats(seat_rows, 1, 1, j, i):
                            o_count += 1
                #Check middle left and right
                if j > 0:
                    if check_seats(seat_rows, -1, 0, j, i):
                        o_count += 1
                if j < len(seat_rows[i]) - 1:
                    if check_seats(seat_rows, 1, 0, j, i):
                        o_count += 1
                #If all adjacent are unoccupied, then occupy the seat
                if o_count >= 5:
                    seat_rows[i][j] = "E"
                    changed = True
    for i in range(0, len(seat_rows)):
        #print("Running...")
        for j in range(0, len(seat_rows[i])):
            if seat_rows[i][j] == "X":
                seat_rows[i][j] = "#"
            elif seat_rows[i][j] == "E":
                seat_rows[i][j] = 'L'
                
    if not changed:
        unchanged = True
    """
    print("\n\n\n\n\n")
    for r in seat_rows:
        print("".join(r))
    input()
    """
    
o = 0
for r in seat_rows:
    print("".join(r))
    c_ = 0
    for c in r:
        if c == "#":
            o += 1
            c_ += 1
    #print(c_)
    #input()
print(o)
#print(time)
    