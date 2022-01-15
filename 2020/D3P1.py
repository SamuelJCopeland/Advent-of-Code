#Advent of Code
#Day 3

tree_file = open("trees.txt",'r')
tree_rows = tree_file.readlines()

col_pos = 0
row_pos = 0
trees = [0,0,0,0,0]
#print(len(tree_rows[0]))
for i in range(0, len(tree_rows)):
    tree_rows[i] = tree_rows[i][:-1]
    if tree_rows[i][col_pos] == "#":
        trees[0] = trees[0] + 1
    col_pos += 3
    if col_pos >= len(tree_rows[i]):
        col_pos = col_pos - len(tree_rows[i])
    
    #print(tree_rows[i])
    #print(tree_rows[i][col_pos])
    #print(i)
    #print(col_pos)
    #input("next")
    
#print(trees)
col_pos = 0
for i in range(0, len(tree_rows)):
    if tree_rows[i][col_pos] == "#":
        trees[1] = trees[1] + 1
    col_pos += 1
    if col_pos >= len(tree_rows[i]):
        col_pos = col_pos - len(tree_rows[i])
    
        
col_pos = 0
for i in range(0, len(tree_rows)):
    if tree_rows[i][col_pos] == "#":
        trees[2] = trees[2] + 1
    col_pos += 5
    if col_pos >= len(tree_rows[i]):
        col_pos = col_pos - len(tree_rows[i])
    #print(i)
    #print(col_pos)
    #input("next")
        
col_pos = 0
for i in range(0, len(tree_rows)):
    if tree_rows[i][col_pos] == "#":
        trees[3] = trees[3] + 1
    col_pos += 7
    if col_pos >= len(tree_rows[i]):
        col_pos = col_pos - len(tree_rows[i])      
col_pos = 0
print(len(tree_rows[0]))
for i in range(0, len(tree_rows), 2):
    if tree_rows[i][col_pos] == "#":
        trees[4] = trees[4] + 1
    col_pos += 1
    if col_pos >= len(tree_rows[i]):
        col_pos = col_pos - len(tree_rows[i])
    
print(trees)
total = 1
for ent in trees:
    total = total * ent
print(total)