data = []
with open("p2.txt", "r") as input_file:
    for l in input_file:
        data.append(l)
input_file.close()
total = 0
ribbon = 0
for l in data:
    #2*l*w + 2*w*h + 2*h*l
    surfaces = []
    dims = l[:-1].split("x")
    surfaces.append(int(dims[0])*int(dims[1]))
    surfaces.append(int(dims[1])*int(dims[2]))
    surfaces.append(int(dims[0])*int(dims[2]))
    sides = []
    for d in dims:
        sides.append(int(d))
    sides.sort()
    total += min(surfaces)
    total += (surfaces[0] + surfaces[1] + surfaces[2]) * 2
    ribbon += 2*sides[0] + 2*sides[1]+ sides[0]*sides[1]*sides[2]
print(total)
print(ribbon)