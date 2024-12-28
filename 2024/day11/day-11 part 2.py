import os
path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"day-11 input.txt")
stones = {}

#use this to switch between parts
part = 2
with open (path, 'r') as d:
    line = d.readline()

    for i in range(len(line.strip().split(" "))):
        stones.setdefault(line.strip().split(" ")[i], 0)
        stones[line.strip().split(" ")[i]] += 1
    d.close()
    
def ChangeStones(stoneList = {}):
    newStones = {}

    for i in stoneList.keys():
        stoneNum = int(i)
        stoneString = i
        
        if (stoneString == "0"):
            newStones.setdefault("1", 0)
            newStones["1"] += stoneList[stoneString]
        elif (len(stoneString) % 2 == 0):
            firstpart  = stoneString[:len(stoneString)//2]
            secondpart = stoneString[len(stoneString)//2:]
            newStones.setdefault(firstpart, 0)
            newStones[firstpart] += stoneList[stoneString]
            if (int(secondpart) == 0):
                newStones.setdefault("0", 0)
                newStones["0"] += stoneList[stoneString]
            else:
                newStones.setdefault(str(int(secondpart)), 0)
                newStones[str(int(secondpart))] += stoneList[stoneString]
        else:
            newStones.setdefault(str(stoneNum * 2024), 0)
            newStones[str(stoneNum * 2024)] += stoneList[stoneString]
    return newStones

stoneList = stones

blinks = 1000
for i in range(blinks):
    print(f"Blink: {i + 1} / {blinks}")
    stoneList = ChangeStones(stoneList)
    
answer = 0
for i in stoneList.keys():
    answer += stoneList[i]
#print(stoneList)
print(answer)