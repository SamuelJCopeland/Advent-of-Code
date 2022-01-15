with open("P3.txt", "r") as file:
    epsilon = ""
    gamma = ""
    one_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    zero_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    oxygen_list = []
    lines = []
    co2_list = []
    for line in file:
        oxygen_list.append(line)
        co2_list.append(line)
        lines.append(line)
        for i in range(0, 12):
            if line[i] == '1':
                one_count[i] += 1
            else:
                zero_count[i] += 1
                
    for i in range(0, 12):
        if one_count[i] > zero_count[i]:
            gamma += ("1")
            epsilon += ("0")
        else:
            gamma += ("0")
            epsilon += ("1")
        to_remove = []
        if len(oxygen_list) > 1:
            o_count = 0
            z_count = 0
            for n in oxygen_list:
                if n[i] == "1":
                    o_count += 1
                else:
                    z_count += 1
            if o_count >= z_count:
                for n in oxygen_list:
                    if n[i] == '0':
                        to_remove.append(n)
            else:
                for n in oxygen_list:
                    if n[i] == '1':
                        to_remove.append(n)
        for n in to_remove:
            oxygen_list.remove(n)
        
        to_remove = []
        if len(co2_list) > 1:
            o_count = 0
            z_count = 0
            for n in co2_list:
                if n[i] == "1":
                    o_count += 1
                else:
                    z_count += 1
            
            if z_count <= o_count:
                for n in co2_list:
                    if n[i] == '1':
                        to_remove.append(n)
            else:
                for n in co2_list:
                    if n[i] == '0':
                        to_remove.append(n)
        for n in to_remove:
            co2_list.remove(n)
    epsilon = int(epsilon, 2)
    gamma = int(gamma, 2)
    oxygen = int(oxygen_list[0], 2)
    co2 = int(co2_list[0], 2)
    
    print(epsilon * gamma)
    print(oxygen * co2)