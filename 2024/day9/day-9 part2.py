import os
path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"day-9 input.txt")
numbers = []
with open (path, 'r') as d:
    line = d.readline()
    numbers = list(line)
    numbers = list(map(int, numbers))
    d.close()
    
def GetFullString(nums):
    finalString = []
    id = 0
    
    for i in range(len(nums)):
        if (nums[i] == 0):
            continue
        
        if i % 2 == 0:
            #is data
            tempList = []
            for x in range(nums[i]):
                tempList.append(str(id))
            finalString.append(tempList)
            id += 1
        else:
            #isnt data
            tempList = []
            for x in range(nums[i]):
                tempList.append(".")
            finalString.append(tempList)
    
    return finalString

def CompactString(numString = []):
    compactedString = []
    compactedString = numString
    def IsNum(strjngyeehaw):
        for i in range(len(strjngyeehaw)):
            if (not strjngyeehaw[i][0].isdigit()):
                return False
        return True
    
    def GetBlankList(length):
        thing = []
        for i in range(length):
            thing.append(".")
        
        return thing
    start = len(compactedString)
    while not IsNum(compactedString):
        for i in range(start - 1, -1, -1):
            if (compactedString[i][0].isdigit()):
                for x in range(len(compactedString)):
                    if (x >= start - 1):
                        break
                    if (compactedString[x][0].isdigit() == False):
                        
                        difference = len(compactedString[i])
                        if (len(compactedString[x]) == len(compactedString[i])):
                            compactedString[x] = compactedString[i]
                            if (i == len(compactedString) - 1):
                                compactedString.pop(len(compactedString)-1)
                            else:
                                compactedString[i] = GetBlankList(len(compactedString[i]))
                            break
                        elif (len(compactedString[x]) > len(compactedString[i])):
                            oldNum = compactedString[i]
                            if (i == len(compactedString) - 1):
                                compactedString.pop(len(compactedString)-1)
                            else:
                                compactedString[i] = GetBlankList(len(compactedString[i]))
                            
                            for z in range(len(oldNum)):
                                compactedString[x].pop(len(compactedString[x])-1)
                            compactedString.insert(x, oldNum)
                            break
                start -= 1
                break    
        if (start == 0):
            break
    return compactedString



def GetCheckSum(numString = []):
    numList = []
    for i in range(len(numString)):
        for x in range(len(numString[i])):
            numList.append(numString[i][x])

    sum = 0
    for i in range(len(numList)):
        if (numList[i].isdigit()):
            sum += int(numList[i]) * i
    
    return sum

print(GetCheckSum(CompactString(GetFullString(numbers))))