def simulateMovement(h, i, dir, knots):
    t = knots[i]
    if dir == 'U':
        # If tail is still in same column, and there is a one space gap, move the tail up one
        if h[1] == t[1] and abs(h[0] - t[0]) == 2:
            t[0] -= 1
            if i < 8:
                simulateMovement(t, i+1, dir, knots)
        #Else, if the vertical distance is 2 and they are not in the same column, up one and move to the same column
        elif h[1] != t[1] and abs(h[0] - t[0]) == 2:
            t[0] -= 1
            newP = h[1]-t[1]
            newD = ''
            if newP < 0:
                newD = 'L'
                t[1] -= 1
            else:
                newD = 'R'
                t[1] += 1
            if i < 8:
                simulateMovement(t, i+1, dir, knots)
                simulateMovement(t, i+1, newD, knots)

    elif dir == 'D':
        # If tail is still in same column, and there is a one space gap, move the tail down one
        if h[1] == t[1] and abs(h[0] - t[0]) == 2:
            t[0] += 1
            if i < 8:
                simulateMovement(t, i+1, dir, knots)
        #Else, if the vertical distance is 2 and they are not in the same column, down one and move to the same column
        elif h[1] != t[1] and abs(h[0] - t[0]) == 2:
            t[0] += 1

            newP = h[1]-t[1]
            newD = ''
            if newP < 0:
                newD = 'L'
                t[1] -= 1
            else:
                newD = 'R'
                t[1] += 1

            if i < 8:
                simulateMovement(t, i+1, dir, knots)
                simulateMovement(t, i+1, newD, knots)
    elif dir == 'L':
        # If tail is still in same row, and there is a one space gap, move the tail left one
        if h[0] == t[0] and abs(h[1] - t[1]) == 2:
            t[1] -= 1
            if i < 8:
                simulateMovement(t, i+1, dir, knots)
        #Else, if the horizontal distance is 2 and they are not in the same row, left one and move to the same row
        elif h[0] != t[0] and abs(h[1] - t[1]) == 2:
            t[1] -= 1

            newP = h[0]-t[0]
            newD = ''
            if newP < 0:
                newD = 'U'
                t[0] -= 1
            else:
                newD = 'D'
                t[0] += 1
            if i < 8:
                simulateMovement(t, i+1, dir, knots)
                simulateMovement(t, i+1, newD, knots)
    elif dir == 'R':
        # If tail is still in same row, and there is a one space gap, move the tail right one
        if h[0] == t[0] and abs(h[1] - t[1]) == 2:
            t[1] += 1
            if i < 8:
                simulateMovement(t, i+1, dir, knots)
        #Else, if the horizontal distance is 2 and they are not in the same row, move right one and move to the same row
        elif h[0] != t[0] and abs(h[1] - t[1]) == 2:
            t[1] += 1

            newP = h[0]-t[0]
            newD = ''
            if newP < 0:
                newD = 'U'
                t[0] -= 1
            else:
                newD = 'D'
                t[0] += 1
            if i < 8:
                simulateMovement(t, i+1, dir, knots)
                simulateMovement(t, i+1, newD, knots)
    

h = [0,0]
t = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]
#i is vertical, j is horizontal
positions = ['0,0']
with open(r"2022/input9.txt", "r") as input_file:
    for line in input_file:
        line = line[:-1].split(' ')
        dir = line[0]
        dist = int(line[1])

        for i in range(dist):
            if dir == 'U':
                h[0] -= 1
            elif dir == 'D':
                h[0] += 1
            elif dir == 'L':
                h[1] -= 1
            elif dir == 'R':
                h[1] += 1
                
            simulateMovement(h, 0, dir, t)           

            pos = str(t[8][0]) + ',' + str(t[8][1])
            if not pos in positions:
                positions.append(pos)
print(len(positions))