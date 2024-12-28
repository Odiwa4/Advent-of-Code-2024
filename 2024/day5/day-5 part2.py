import os
pathRules = os.path.join(os.path.dirname(os.path.abspath(__file__)),"day-5 rules.txt")
pathOrders= os.path.join(os.path.dirname(os.path.abspath(__file__)),"day-5 orders.txt")

ruleDict = {}
orders = [] 
with open (pathRules, 'r') as d:
    lines = d.readlines()

    for i in range(len(lines)):
        splitString = lines[i].strip().split("|")
        ruleDict[int(splitString[0])] = []
    for i in range(len(lines)):
        splitString = lines[i].strip().split("|")
        ruleDict[int(splitString[0])].append(int(splitString[1]))
    d.close()
    
with open (pathOrders, 'r') as d:
    lines = d.readlines()

    for i in range(len(lines)):
        orders.append(lines[i].strip().split(","))

    orders[i] = [int(item) for item in orders[i]]
    d.close()

def IsOrderValid(order):
    for o in range(len(order)):
        if (o == 0):
            continue
        
        for i in range(o):
            if (int(order[o]) in ruleDict.keys()):
                for d in ruleDict.get(int(order[o])):
                    #print(str(order[i]) + " | " + str(d))
                    if (int(order[i]) == int(d)):
                        return False
    return True

def GetErrors(order):
    newOrder = order
    
    if (IsOrderValid(order)):
        return newOrder
    for o in range(len(order)):
        if (o == 0):
            continue
        
        for i in range(o):
            if (int(order[o]) in ruleDict.keys()):
                for d in ruleDict.get(int(order[o])):
                    #print(str(order[i]) + " | " + str(d))
                    if (int(order[i]) == int(d)):
                        newList = order.copy()
                        newList[i] = order[o]
                        newList[o] = order[i]
                        newOrder = newList.copy()

                        if (not IsOrderValid(newOrder)):
                            result = GetErrors(newOrder)
                            if result:
                                return result
                        else:
                            return newOrder
    return newOrder

def GetMiddle(order):
    return order[int((len(order)) / 2)]

orderIdTest = 5

answer = 0
for o in range(len(orders)): 
    if (not IsOrderValid(orders[o])):
        print(GetErrors(orders[o]))
        answer += int(GetMiddle(GetErrors(orders[o])))

print(answer)