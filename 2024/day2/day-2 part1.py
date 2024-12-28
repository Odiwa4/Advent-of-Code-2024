import os
path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"day-2 input.txt")

reports = []
with open (path, 'r') as d:
    lines = d.readlines()
    for i in range(len(lines)):
        reports.append(lines[i].strip().split(" "))
        reports[i] = [int(item) for item in reports[i]]
    d.close()

def CheckSafe(list):
    #EITHER ALL DECREASING OR ALL INCREASING
    #NUMBERS DONT INCREASE/DECREASE MORE THAN 3
    #IF ONE NUMBER CAN BE REMOVED TO FIX IT, IT PASSES
    
    lastDifference = 0
    for i in range(len(list)):
        increasing = True
        if (i == len(list) - 1):
            break
        
        #all increasing / all decreasing
        difference = list[i] - list[i+1]
        if (difference > 3 or difference < -3 or difference == 0):
            return False
        if (lastDifference != 0):
            if ((lastDifference > 0 and difference < 0) or (lastDifference < 0 and difference > 0)):
                return False
        lastDifference = difference
    return True

print(CheckSafe([1, 3, 6, 7, 8]))

safeCount = 0
for r in range(len(reports)):
   if (CheckSafe(reports[r]) == True):
        safeCount += 1

print(safeCount)
