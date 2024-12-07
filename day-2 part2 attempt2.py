import os
path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"day-2 input.txt")

reports = []
with open (path, 'r') as d:
    lines = d.readlines()
    for i in range(len(lines)):
        reports.append(lines[i].strip().split(" "))
        reports[i] = [int(item) for item in reports[i]]
    d.close()

def GetWrong(report):
    #EITHER ALL DECREASING OR ALL INCREASING
    #NUMBERS DONT INCREASE/DECREASE MORE THAN 3
    #IF ONE NUMBER CAN BE REMOVED TO FIX IT, IT PASSES
    wrongIndexes = []
    lastDifference = 0
    for i in range(len(report)):
        if (i == len(report) - 1):
            break
        
        #all increasing / all decreasing
        difference = report[i] - report[i+1]
        if (difference > 3 or difference < -3 or difference == 0):
            wrongIndexes.append(i)
            wrongIndexes.append(i+1)
        if (lastDifference != 0):
            if ((lastDifference > 0 and difference < 0) or (lastDifference < 0 and difference > 0)):
                wrongIndexes.append(i)
                wrongIndexes.append(i+1)
        lastDifference = difference

    wrongIndexes = list(dict.fromkeys(wrongIndexes.copy()))
    return wrongIndexes

def CheckSafe(report):
    wrong = GetWrong(report)
    print(wrong)
    for i in range(len(wrong)):
        newList = []
        for x in range(len(report)):
            if (x != wrong[i]):
                newList.append(report[x])
        if (len(GetWrong(newList)) == 0):
            return True
    firstList = []
    for x in range(len(report)):
        if (x != 0):
            firstList.append(report[x])
    if (len(GetWrong(firstList)) == 0):
        return True
    else:
        return False
    
#print(CheckSafe([48, 46, 47, 49, 51, 54, 56]))

safeCount = 0
for r in range(len(reports)):
   if (CheckSafe(reports[r]) == True):
        #print("SAFE" + str(r + 1))
        safeCount += 1

print(safeCount)
