import os
path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"Tday-11 input.txt")
stones = []

#use this to switch between parts
part = 2
with open (path, 'r') as d:
    line = d.readline()

    for i in range(len(line.strip().split(" "))):
        stones.append(line.strip().split(" ")[i])
    print(stones)
    d.close()
    
def ChangeStones(stoneList):
    newStones = []
    for i in range(len(stoneList)):
        stoneNum = int(stoneList[i])
        stoneString = stoneList[i]
        
        if (stoneString == "0"):
            newStones.append("1")
        elif (len(stoneString) % 2 == 0):
            firstpart  = stoneString[:len(stoneString)//2]
            secondpart = stoneString[len(stoneString)//2:]
            newStones.append(firstpart)
            if (int(secondpart) == 0):
                newStones.append("0")
            else:
                newStones.append(str(int(secondpart)))
        else:
            newStones.append(str(stoneNum * 2024))
    return newStones

stoneList = stones

for i in range(6):
    #print(f"BLINK: {i + 1} / 75")
    stoneList = ChangeStones(stoneList)
    print(stoneList)
print(len(stoneList))