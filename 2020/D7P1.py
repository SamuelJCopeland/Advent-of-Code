#Advent of Code
#Day 7
#part 1
"""
def find_bags(rule_dict, name = "shiny gold", bags = []):
    all_bags = bags
    total =  0
    for b in rule_dict[name]:
        if not b in all_bags:
            all_bags.append(b)
            total = total + 1
            if b in rule_dict:
                total = total + find_bags(rule_dict, b, all_bags)
    return total

bag_rules = open('bags.txt','r').readlines()

rule_dict = {}

for r in bag_rules:
    temp = r.split(" bags contain ")
    bag = temp[0]
    
    temp = temp[1:]
    t = ''
    for i in temp:
        t = t + i
    temp = t
    contain_bags = temp.split(',')
    in_bags = []
    for b in contain_bags:
        if b[0] == " ":
            b = b[1:]
        b = b.split(" ")[1:-1]
        in_bags.append(' '.join(b))
        b = ' '.join(b)
        if not b in rule_dict:
            rule_dict[b] = []
        rule_dict[b].append(bag)
#temp = open('temp.txt','w')
#temp.write(str(rule_dict))
print(find_bags(rule_dict, "shiny gold"))
"""

def find_bags(rule_dict, name = "shiny gold", bags = []):
    all_bags = bags
    total =  0
    for b in rule_dict[name]:
        if not b in all_bags:
            all_bags.append(' '.join(b.split(" ")[1:]))
            total = total + int(b.split(" ")[0])
            
            if ' '.join(b.split(" ")[1:]) in rule_dict:
                total = total + int(b.split(" ")[0]) * find_bags(rule_dict, ' '.join(b.split(" ")[1:]), all_bags)
    return total

bag_rules = open('bags.txt','r').readlines()

rule_dict = {}

for r in bag_rules:
    temp = r.split(" bags contain ")
    bag = temp[0]
    
    temp = temp[1:]
    t = ''
    for i in temp:
        t = t + i
    temp = t
    in_bags = []
    if temp != "no other bags.\n":
        contain_bags = temp.split(',')
        for b in contain_bags:
            if b[0] == " ":
                b = b[1:]
            b = b.split(" ")[:-1]
            in_bags.append(' '.join(b))
            b = ' '.join(b)
    rule_dict[bag] = in_bags
    
temp = open('temp.txt','w')
temp.write(str(rule_dict))
print(find_bags(rule_dict, "shiny gold"))
