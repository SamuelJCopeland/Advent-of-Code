import hashlib
  
# encoding GeeksforGeeks using md5 hash
# function 
letters = 'yzbqklnj'

  
found = False
current = 1
while not found:
    temp = letters + str(current)
    result = hashlib.md5(temp.encode())
    result = result.hexdigest()
    #input(result)
    if result[:6] == "000000":
        print(current)
        found = True
    else:
        current += 1