#Advent of Code
#Day 17
"""
def removeNewline(inputString):
    if inputString[-1] == '\n':
        return inputString[:-1]
    else:
        return inputString

pInput = list(map(removeNewline, open("cubes.txt",'r').readlines()))
cubes = [[ ['.' for col in range(100)] for col in range(100)] for row in range(100)]

for i in range(0, len(pInput)):
    for j in range(0, len(pInput[0])):
        cubes[i][j][0] = pInput[i][j]
active = 0
for r in range(0, 6):
    active = 0
    for i in range(0, len(cubes)):
        for j in range(0, len(cubes[i])):
            for k in range(0, len(cubes[i][j])):
                total = 0
                for l in range(i - 1, i + 2):
                    for m in range(j - 1, j + 2):
                        for n in range(k - 1, k + 2):
                            if not (l == i and m == j and n == k) and l < 100 and m < 100 and n < 100:
                                try:
                                    if cubes[l][m][n] == '#' or cubes[l][m][n] == 'i':
                                        total += 1
                                except:
                                    print(l)
                                    print(m)
                                    print(n)
                if cubes[i][j][k] == '.':
                    if total == 3:
                        cubes[i][j][k] == 'a'
                elif cubes[i][j][k] == "#":
                    if total < 2 or total > 3:
                        cubes[i][j][k] = 'i'
    for i in range(0, 100):
        for j in range(0, 100):
            for k in range(0, 100):
                if cubes[i][j][k] == "a":
                    cubes[i][j][k] = '#'
                elif cubes[i][j][k] == "i":
                    cubes[i][i][k] = '.'
                
                if cubes[i][j][k] == '#':
                    active += 1
print(active)
"""
"""
---PART ONE---
"""
"""
PSEUDOCODE
create a list of lists of lists which has at the center the puzzle input; 
      around it there're 6 more lines/column for each side. These ones are void('.')
apply conditions
NOTES
structure of the space:
      y[
            x[
                  z[
                        
                  ]
            ]
      ]
"""
from itertools import product
from collections import defaultdict

initial = """
...#.#.#
..#..#..
#.#.##.#
###.##..
#####.##
#.......
#..#..##
...##.##
""".strip()


def neighborhood(*position: int):
    for diff in product([-1, 0, 1], repeat=len(position)):
        neighbor = tuple(pos + diff[i] for i, pos in enumerate(position))
        yield neighbor


def full_cycle(initial, dimensions):
    space = defaultdict(lambda: ".")
    padding = (0,) * (dimensions - 2)
    for x, line in enumerate(initial.splitlines()):
        for y, state in enumerate(line):
            cube = (x, y) + padding
            space[cube] = state

    for _ in range(6):
        cube_to_active_count = defaultdict(int)

        for cube in space:
            if space[cube] == ".":
                continue
            for n in neighborhood(*cube):
                # neighborhood contains cube and all its neighbors.
                # `cube_to_active_count[n] += n != cube` ensures
                # active cubes without active neighbors are counted
                # and proper deactivated by underpopulation in the
                # next for-loop.
                cube_to_active_count[n] += n != cube and space[cube] == "#"
        for n, count in cube_to_active_count.items():
            if space[n] == "#":
                if count in [2, 3]:
                    space[n] = "#"
                else:
                    space[n] = "."
            elif space[n] == ".":
                if count == 3:
                    space[n] = "#"

    return sum(state == "#" for state in space.values())


print("--- part 1 ---")
print(full_cycle(initial, 3))
print("--- part 2 ---")
print(full_cycle(initial, 4))