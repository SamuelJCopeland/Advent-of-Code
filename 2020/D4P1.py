#Advent of Code
#Day 4

import re
def special_match(strg, search=re.compile(r'[^a-f0-9.]').search):
    return not bool(search(strg))

pass_file = open("passports.txt", 'r')
lines = pass_file.readlines()
#print(lines)
index = 0
passports = []
for l in lines:
    if l == "\n":
        index = index + 1
    else:
        if len(passports) >= index + 1:
            passports[index] = passports[index] + l[:-1] + " "
        else:
            passports.append(l[:-1] + " ")

valid_passports = 0

for p in passports:
    year_g = False
    i_year_g = False
    e_year_g = False
    h_good = False
    hair_g = False
    eye_g = False
    pid_g = False
    if(p.find("byr:") >= 0 and p.find("iyr") >= 0 and p.find("eyr:") >= 0 and p.find("hgt:") >= 0 and p.find("ecl:") >= 0 and p.find("pid:") >= 0 and p.find("hcl:") >= 0):
        
        by_index = p.find("byr:") + 4
        
        if by_index + 4 == len(p) or (by_index + 4 < len(p) and p[by_index + 4] == ' '):
            birth_y = int((p[by_index:by_index + 4]))
            
            if birth_y >= 1920 and birth_y <= 2002:
                year_g = True
        
        iy_index = p.find("iyr:") + 4
        
        if iy_index + 4 == len(p) or (iy_index + 4 < len(p) and p[iy_index + 4] == ' '):
            issue_y = int((p[iy_index:iy_index + 4]))
            if issue_y >= 2010 and issue_y <= 2020:
                i_year_g = True
                
        ey_index = p.find("eyr:") + 4
        
        if ey_index + 4 == len(p) or (ey_index + 4 < len(p) and p[ey_index + 4] == ' '):
            exp_y = int((p[ey_index:ey_index + 4]))
            if exp_y >= 2020 and exp_y <= 2030:
                e_year_g = True
        
        h_index = p.find("hgt:") + 4
        
        
        if (h_index + 6 == len(p) and p[h_index + 3:h_index + 5] == "cm") or (h_index + 6 < len(p) and p[h_index + 3:h_index + 6] == "cm "):
            hgt = int((p[h_index:h_index + 3]))
            
            if hgt >= 150 and hgt <= 193:
                h_good = True
        elif (h_index + 4 == len(p) and p[h_index + 2:h_index + 4] == "in") or (h_index + 5 < len(p) and p[h_index + 2:h_index + 5] == "in "):
            hgt = int((p[h_index:h_index + 2]))
            if hgt >= 59 and hgt <= 76:
                h_good = True
                
        hc_index = p.find("hcl:") + 4
        
        
        if (hc_index + 7 == len(p) and p[hc_index] == "#") or (hc_index + 7 < len(p) and p[hc_index] == "#" and p[hc_index + 7] == " "):
            #print(p[hc_index + 1:])
            #input()
            check = p[hc_index + 1:hc_index + 7]
            if special_match(check):
                hair_g = True
            """
            hgt = int((p[h_index:h_index + 3]))
            if hgt >= 150 and hgt <= 193:
                h_good = True
            """
        ec_index = p.find("ecl:") + 4
        print(p[ec_index:ec_index + 3])
        #print(p[hc_index:])
        #input()
        
        if (ec_index + 3 == len(p)) or (ec_index + 3 < len(p) and p[ec_index + 3] == " "):
            c = p[ec_index:ec_index + 3]
            if c == 'amb' or c == 'blu' or c == 'brn' or c == 'gry' or c == 'grn' or c == 'hzl' or c == 'oth':
                eye_g = True
                print("eye good")
        
        pid_index = p.find("pid:") + 4
        
        if pid_index + 9 == len(p) or (pid_index + 9 < len(p) and p[pid_index + 9] == ' '):
            pid = (p[pid_index:pid_index + 9])
            if(special_match(pid, re.compile(r'[^0-9.]').search)):
                pid_g = True
        
        print(year_g)
        print(i_year_g)
        print(e_year_g)
        print(h_good)
        print(hair_g)
        print(eye_g)
        print(pid_g)
        print("\n")
        
        if year_g and i_year_g and e_year_g and h_good and hair_g and eye_g and pid_g:
            valid_passports = valid_passports + 1
               
print(valid_passports)