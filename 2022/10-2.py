x = 1
cycle = 0
screen_width = 40
screen = ''
with open(r"2022/input10.txt", "r") as input_file:
    for line in input_file:
        line = line[:-1].split(' ')
        if line[0] == 'addx':
            if cycle % screen_width == 0:
                screen += '\n'
            
            pos = cycle % screen_width

            if x-1 ==  pos or x == pos or x+1 == pos:
                screen += '#'
            else:
                screen += '.'

            cycle += 1

            if cycle % screen_width == 0:
                screen += '\n'

            pos = cycle % screen_width

            if x-1 ==  pos or x == pos or x+1 == pos:
                screen += '#'
            else:
                screen += '.'
            
            x += int(line[1])

            cycle += 1
        else:
            if cycle % screen_width == 0:
                screen += '\n'

            pos = cycle % screen_width

            if x-1 ==  pos or x == pos or x+1 == pos:
                screen += '#'
            else:
                screen += '.'
            
            cycle += 1
print(screen)