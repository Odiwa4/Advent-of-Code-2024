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
            for x in range(nums[i]):
                finalString.append(str(id))
            id += 1
        else:
            #isnt data
            for x in range(nums[i]):
                finalString.append(".")
    
    return finalString

def CompactString(numString = ""):
    compactedString = list(numString)
    def IsNum(strjngyeehaw):
        for i in range(len(strjngyeehaw)):
            if (not strjngyeehaw[i].isdigit()):
                return False
        return True
    while not IsNum(compactedString):
        dotIndex = -1
        for i in range(len(compactedString)):
            if (compactedString[i] == "."):
                print(i)
                dotIndex = i
                break
            
        for i in range(len(compactedString) - 1, -1, -1):
            if (compactedString[i].isdigit()):
                #print(compactedString[i])
                compactedString[dotIndex] = compactedString[i]
                compactedString.pop(len(compactedString)-1)
                #print(compactedString)
                break    
            else:
                compactedString.pop(len(compactedString)-1)
    return compactedString

def GetCheckSum(numString = ""):
    numList = list(map(int, numString))
    sum = 0
    
    for i in range(len(numList)):
        sum += numList[i] * i
        
    return sum
print(GetFullString(numbers))
print(GetCheckSum(CompactString(GetFullString(numbers))))
