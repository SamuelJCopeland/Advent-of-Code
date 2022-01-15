#Advent of Code 
#Day 2

passwords_list = open("passwords.txt", 'r').readlines()

valid_passwords = 0

for p in passwords_list:
    p_and_r = p.split(' ')
    num_min = int(p_and_r[0].split('-')[0])
    num_max = int(p_and_r[0].split('-')[1])
    letter = p_and_r[1][:-1]
    passw = p_and_r[2]
    if (passw[num_min - 1] == letter and passw[num_max-1] != letter) or (passw[num_min - 1] != letter and passw[num_max-1] == letter):
        valid_passwords = valid_passwords + 1
        
print(valid_passwords)