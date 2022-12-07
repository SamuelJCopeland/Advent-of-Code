
def changeDir(path, files):
    d = files
    for c in path:
        if c in d:
            d = d[c]
        else:
            d[c] = {}
            d = d[c]
    return d

def addFile(path, files, name, size):
    d = files
    for c in path:
        d = d[c]
    d[name] = size

def sum_folders(cur_dir, sums):
    sum = 0
    for i in cur_dir:
        if type(cur_dir[i]) is dict:
            sum += sum_folders(cur_dir[i], sums)
        else:
            sum += cur_dir[i]
    sums.append(sum)
    return sum

files = {'/':{}}
prev_command = ''
dir_path = []
cur_dir = {}

with open(r"2022/input7.txt", "r") as input_file:
    for line in input_file:
        line = line[:-1].split(' ')
        if line[0] == '$':
            prev_command = line[1]
            if prev_command == 'cd':
                dir = line[2]
                if dir == '/':
                    dir_path = ['/']
                elif dir == '..':
                    dir_path = dir_path[:-1]
                else:
                    dir_path.append(dir)
                
                curDir = changeDir(dir_path, files)
        #Still problems with this part
        elif prev_command == 'ls':
            if line[1] not in cur_dir:
                if line[0] == 'dir':
                    dir_path.append(line[1])
                    changeDir(dir_path, files)
                    dir_path = dir_path[:-1]
                else:
                    addFile(dir_path, files, line[1], int(line[0]))
sums = []
total = 0
sum_folders(files['/'], sums)
for s in sums:
    if s <= 100000:
        total += s

print(total)
#print(files)
