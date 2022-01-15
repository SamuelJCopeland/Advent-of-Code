#Advent of Code
#Day 13
from functools import reduce

notes = open("busses.txt",'r')
lines = notes.readlines()
leave_time = int(lines[0][:-1])
busses = lines[1][:-1]
available_busses = []
for i in busses.split(","):
    if i.isnumeric():
        available_busses.append(int(i))
print(leave_time)
print(available_busses)
shortest_wait = 1000000000000
shortest_bus = 0
for b in available_busses:
    timestamp = 0
    while timestamp < leave_time:
        timestamp += b
    if timestamp - leave_time < shortest_wait:
        shortest_wait = timestamp - leave_time
        shortest_bus = b
        
#print(shortest_bus * shortest_wait)
"""
def check_times(target_time = 0, prev_i = 0, next_i = 0, bus = []):
    if bus[next_i].isnumeric():
        b = int(bus[next_i])
        timestamp = 0
        while timestamp <= target_time:
            timestamp += b
        #print(str(timestamp - target_time) + "\t" + str(next_i - prev_i) + "\t" + str(b))
        if timestamp - target_time == next_i - prev_i:
            prev_i = next_i
            next_i += 1
            if next_i < len(bus):
                #print("yes\t" + str(b))
                return check_times(timestamp, prev_i, next_i, bus)
            else:
                return True
        else:
            return False
    else:
        return check_times(target_time, prev_i, next_i + 1, bus)
busses = busses.split(",")
timestamp = 0
while timestamp < 100000000000000:
    timestamp += int(busses[0])
while not check_times(timestamp, 0, 1, busses):
    #print(timestamp)
    timestamp += int(busses[0])
    
print(timestamp)
"""
def parse_input(data):
    return [int(x) if x.isdigit() else x for x in data.split(',')]
data = parse_input(busses)
def part_two(data):
    buses = [x for x in data if type(x) is int]
    mods = [-i%v for i, v in enumerate(data) if v!='x']
    x, step = 0, 1
    for d, r  in zip(buses, mods):
        while x % d != r:
            x += step
        step *= d
    return x
print(f'Part 2: {part_two(data)}')