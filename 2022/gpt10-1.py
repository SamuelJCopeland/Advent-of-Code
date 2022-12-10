# initialize the program list
program = []

# open the input file and read the program
with open(r"2022/input10.txt", "r") as input_file:
  for line in input_file:
    program.append(line.split())

# initialize the X register, the cycle counter, and the sum variable
x = 1
cycle = 0
sum = 0

# execute the program
for instr, *args in program:
  if instr == "noop":
    # noop instruction does nothing
    cycle += 1
    # check if the current cycle is a 20th, 60th, 100th, etc. cycle
    if cycle % 40 == 20:
      # add the signal strength to the sum
      sum += cycle * x
  elif instr == "addx":
    # increment the cycle counter by 1 and check if the current cycle is
    # a 20th, 60th, 100th, etc. cycle
    cycle += 1
    if cycle % 40 == 20:
      # add the signal strength to the sum
      sum += cycle * x
    # increment the cycle counter by 1 again, check if the current cycle
    # is a 20th, 60th, 100th, etc. cycle, and update the X register
    cycle += 1
    if cycle % 40 == 20:
      # add the signal strength to the sum
      sum += cycle * x
    x += int(args[0])

# print the sum of the signal strength
print(sum)
