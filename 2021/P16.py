def processPackets(p, s=0, versions=[]):
    #print(p)
    #print(s)
    #print("Version: " + str(int(p[:3],2)))
    versions.append(int(p[:3],2))
    packetEnds = []
    pType = int(p[3:6],2)
    #print("pType = " + str(pType))
    if pType != 4:
        
        if p[6] == '0':
            length = int(p[7:22],2)
            #input("length = " + str(length))
            prevEnd=21
            packetEnds += processPackets(p[prevEnd+1:],prevEnd+1, versions)
            #input("test: " + str(s) + ", " + str(packetEnds[-1] - 21))
            while packetEnds[-1] - 21 < length:
                prevEnd=packetEnds[-1]              
                packetEnds += processPackets(p[prevEnd+1:],prevEnd+1, versions)
                #input("test: " + str(s) + ", " + str(packetEnds[-1] - 21))
            
        else:
            numPackets = int(p[7:18],2)
            #input("numPackets = " + str(numPackets))
            tPackets=1
            prevEnd=17
            packetEnds += processPackets(p[prevEnd+1:],prevEnd+1, versions)
            while tPackets < numPackets:
                prevEnd=packetEnds[-1]
                packetEnds += processPackets(p[prevEnd+1:],prevEnd+1, versions)
                tPackets += 1
    else:
        packetEnds.append(findEndOfLiterals(p[6:])+6)
        #input(packetEnds)
    packetEnds[-1] += s
    return packetEnds
def findEndOfLiterals(p):
    #print("literal")
    #input(p)
    for i in range(0, len(p), 5):
        if p[i] == '0':
            #print(i + 4)
            return i + 4

hexToBin = {'0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101', '6':'0110', '7':'0111', '8':'1000', '9':'1001', 'A':'1010','B':'1011', 'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}
result=""
with open("P16.txt", "r") as file:
    for c in file.readline()[:-1]:
        result += hexToBin[c]
file.close()
#print(result)
versions = []
processPackets(result, 0, versions)
total = 0
for n in versions:
    total += n
print(total)