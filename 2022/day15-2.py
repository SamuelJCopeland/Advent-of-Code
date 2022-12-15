min_x = 9999999999
max_x = 0
min_y = 9999999999
max_y = 0
map = {}
beacon_dist = {}
with open(r"2022/input15.txt", "r") as input_file:
    for line in input_file:
        line = line[:-1].split(' ')
        s_x = line[2].split('=')[1][:-1]
        s_y = line[3].split('=')[1][:-1]
        
        min_x = min(min_x, int(s_x))
        max_x = max(max_x, int(s_x))
        min_y = min(min_y, int(s_y))
        max_y = max(max_y, int(s_y))

        b_x = line[8].split('=')[1][:-1]
        b_y = line[9].split('=')[1]
        
        min_x = min(min_x, int(b_x))
        max_x = max(max_x, int(b_x))
        min_y = min(min_y, int(b_y))
        max_y = max(max_y, int(b_y))

        map[s_x+','+s_y] = 'S'
        map[b_x+','+b_y] = 'B'

        beacon_dist[s_x+','+s_y] = max(int(s_x), int(b_x)) - min(int(s_x), int(b_x)) + max(int(s_y), int(b_y)) - min(int(s_y), int(b_y))

print(f'Min X: {min_x}, Min Y: {min_y}')
print(f'Max X: {max_x}, Max Y: {max_y}')
print()

min_p = 0
max_p = 4000000
solved = False

#Attempt 4
#Work around the edges of all the sensors and check against the ranges of all of the other sensors.
for b in beacon_dist:

    dist = beacon_dist[b] + 1
    b = b.split(',')
    s_x = int(b[0])
    s_y = int(b[1])

    

    l_j = s_x - dist + s_y-(s_y - dist)+1
    r_j = s_x + dist - s_y+(s_y - dist)-1

    for i in range(s_y - dist, s_y + dist+1):
        if i < min_p:
            continue
        elif i > max_p:
            break

        if i <= s_y:
            l_j -= 1
            r_j += 1
        else:
            l_j += 1
            r_j -= 1
        
        if l_j >= min_p and l_j <= max_p:
            found = True
            for k in beacon_dist:      
                dist = beacon_dist[k]
                k = k.split(',')
                s_x = int(k[0])
                s_y = int(k[1])

                if i < s_y:
                    if i > s_y - dist-1 and i < s_y + dist+1 and l_j > s_x - dist - 1+s_y-i and l_j < s_x + dist + 1 - s_y+i:
                        found = False
                        break
                else:
                    if i > s_y - dist-1 and i < s_y + dist+1 and l_j >s_x - dist - 1+i-s_y and l_j < s_x + dist + 1 - i+s_y:
                        found = False
                        break
                
            if found:
                print(l_j*4000000+i)
                solved = True
                break
        if solved:
            break

        if r_j >= min_p and r_j <= max_p:
            found = True
            for k in beacon_dist:      
                dist = beacon_dist[k]
                k = k.split(',')
                s_x = int(k[0])
                s_y = int(k[1])

                if i < s_y:
                    if i > s_y - dist-1 and i < s_y + dist+1 and r_j > s_x - dist - 1+s_y-i and r_j < s_x + dist + 1 - s_y+i:
                        found = False
                        break
                else:
                    if i > s_y - dist-1 and i < s_y + dist+1 and r_j >s_x - dist - 1+i-s_y and r_j < s_x + dist + 1 - i+s_y:
                        found = False
                        break
                
            if found:
                print(r_j*4000000+i)
                solved = True
                break
        if solved:
            break
    if solved:
        break
