# Valve class
class Valve:
    open = False
    visited = False
    def __init__(self, name, rate, tunnels):
        self.name = name
        self.rate = rate
        self.tunnels = tunnels

def getMaxFlow(v_name, time_left, valve_map, solutions, curr_flow_rate, temp):
    old_time = time_left
    old_flow = curr_flow_rate
    total_flow = 0
    if time_left == 0:
        solutions[f'{old_time}:{v_name}'] = total_flow
        temp[f'{old_time}:{v_name}'] = f'Flow Rate is: {curr_flow_rate}'
        return total_flow
    
    valve = valve_map[v_name]
    curr_flow_rate = 0
    
    closed_totals = [0]
    #First check what happens if we don't open this valve, and just travel to the next valve
    for v in valve.tunnels:
        if f'{time_left-1}:{v}' in solutions:
            closed_totals.append(solutions[f'{time_left-1}:{v}'])
        else:
            closed_totals.append(getMaxFlow(v, time_left-1, valve_map, solutions, old_flow, temp))

    closed_totals.sort(reverse=True)

    open_totals = [0]
    #Next, if the valve isn't open and the flow rate of the valve is > 0, open the valve and check all of the tunnels again
    if not valve.open and valve.rate > 0:
        valve.open = True
        time_left -= 1
        
        # If we open the valve and time runs out, no extra pressure is released
        if time_left != 0:
            # After the valve is open, we can increase the flow rate
            curr_flow_rate += valve.rate           
            for v in valve.tunnels:
                if f'{time_left-1}:{v}' in solutions:
                    open_totals.append(solutions[f'{time_left-1}:{v}'])
                else:
                    open_totals.append(getMaxFlow(v, time_left-1, valve_map, solutions, curr_flow_rate+old_flow, temp))
        # Close the valve before we return
        valve.open = False

    # Sort the totals to put the max flow first
    open_totals.sort(reverse=True)

    if closed_totals[0] + old_flow * (time_left-1) > open_totals[0] + (curr_flow_rate+old_flow) * (time_left-1):        
        temp[f'{old_time}:{v_name}'] = f'Flow Rate is: {old_flow}'
        total_flow = closed_totals[0]
    else:
        temp[f'{old_time}:{v_name}'] = f'Flow Rate is: {old_flow + curr_flow_rate}'
        total_flow = open_totals[0] + curr_flow_rate * (time_left-1)

    solutions[f'{old_time}:{v_name}'] = total_flow
    return total_flow
    

valve_map = {}
# 1 minute to open a valve, 1 minute to travel down a tunnel
with open(r"2022/input16.txt", "r") as input_file:
    for line in input_file:
        line = line[:-1].split(' ')
        name = line[1]
        rate = int(line[4].split('=')[1][:-1])
        valves = line[9:]
        for i in range(len(valves)):
            if valves[i][-1] == ',':
                valves[i] = valves[i][:-1]
        valve_map[name] = Valve(name, rate, valves)

solutions = {}
temp = {}

max = 31

# for i in range(1, max+1):
#      for v in valve_map:
#          getMaxFlow(v, i, valve_map, solutions, 0, temp)


getMaxFlow('AA', max, valve_map, solutions, 0, temp)

file_out = ''
for key in solutions:
    file_out += (f'{key}:{solutions[key]} - {temp[key]}') + '\n'

test_file = open("test_file_16.txt", 'w')
test_file.write(file_out)
test_file.close()

print(solutions[f'{max}:AA'])
