"""
    [M]             [Z]     [V]    
    [Z]     [P]     [L]     [Z] [J]
[S] [D]     [W]     [W]     [H] [Q]
[P] [V] [N] [D]     [P]     [C] [V]
[H] [B] [J] [V] [B] [M]     [N] [P]
[V] [F] [L] [Z] [C] [S] [P] [S] [G]
[F] [J] [M] [G] [R] [R] [H] [R] [L]
[G] [G] [G] [N] [V] [V] [T] [Q] [F]
 1   2   3   4   5   6   7   8   9 

"""
stacks = ["GFVHPS","GJFBVDZM","GMLJN","NGZVDWP","VRCB","VRSMPWLZ","THP","QRSNCHZV","FLGPVQJ"]

with open(r"2022/input5.txt", "r") as input_file:
    for line in input_file:
        line = line[:-1].split(' ')
        
        amount = int(line[1])
        f = int(line[3])-1
        t = int(line[5])-1
        m = stacks[f][-amount:]
        stacks[f] = stacks[f][:-amount]
        stacks[t] += m
result = ""
for s in stacks:
    result += s[-1]
print(result)