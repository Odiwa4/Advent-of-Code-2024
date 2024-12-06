import os
leftLists = []
rightLists = []

path = f"{os.path.join(os.path.dirname(os.path.abspath(__file__)),"day-1 input.txt")}"
with open (path, 'r') as d:
    lines = d.readlines()
    
    print(len(lines))
    for i in range(len(lines)):
        line = lines[i]
        lists = line.split()
        leftLists.append(int(lists[0]))
        rightLists.append(int(lists[1]))
    d.close()

def SortCheck(list):
    for i in range(len(list)):
        if (i == len(list) - 1):
            break
        elif (list[i] > list[i + 1]):
            return False
    return True

def SortList(unsortedList):
    list = unsortedList.copy()
    sorted = False
    while sorted == False:
        for i in range(len(list)):
            if (i == len(list) - 1):
                break
            elif (list[i] > list[i + 1]):
                templist = list.copy()
                templist[i] = list[i + 1]
                templist[i + 1] = list[i] 
                list = templist.copy()
        if (SortCheck(list) == True):
            sorted = True
    return list

answer = 0

sortone = SortList(leftLists)
sorttwo = SortList(rightLists)

for i in range(len(sortone)):
    if (sortone[i] > sorttwo[i]):
        answer = answer + sortone[i] - sorttwo[i]
    else:
        answer = answer + sorttwo[i] - sortone[i]

print(answer)