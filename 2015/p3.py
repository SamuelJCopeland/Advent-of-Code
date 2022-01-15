data = ""
visited = {"0,0",}
xpos = 0
ypos = 0
rxpos = 0
rypos = 0
with open("p3.txt", "r") as input_file:
	data = input_file.readline()
input_file.close()
alt = True
for c in data:
    if alt:
        if c == "<":
            xpos -= 1
        elif c == ">":
            xpos += 1
        elif c == "v":
            ypos -= 1
        elif c == "^":
            ypos += 1
        temp = str(xpos) + "," + str(ypos)
        if not temp in visited:
            visited.add(temp)
        alt = False
    else:
        if c == "<":
            rxpos -= 1
        elif c == ">":
            rxpos += 1
        elif c == "v":
            rypos -= 1
        elif c == "^":
            rypos += 1
        temp = str(rxpos) + "," + str(rypos)
        if not temp in visited:
            visited.add(temp)
        alt = True
print(len(visited))