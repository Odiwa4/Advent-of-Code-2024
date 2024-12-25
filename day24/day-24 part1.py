import os
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "day-24 input.txt")
wires = {}
#has tuples, (type, input1, input2, output)
instructions = []
with open(path, 'r') as d:
    lines = d.readlines()
    for l, line in enumerate(lines):
        if ": " in line:
            splitLine = line.strip().split(": ")
            wires[splitLine[0]] = int(splitLine[1])
        elif " -> " in line:
            arrowSplit = line.strip().split(" -> ")
            if "XOR" in line:
                split2 = arrowSplit[0].split(" XOR ")
                instructions.append((0, split2[0], split2[1], arrowSplit[1]))
            elif "OR" in line:
                split2 = arrowSplit[0].split(" OR ")
                instructions.append((1, split2[0], split2[1], arrowSplit[1]))
            elif "AND" in line:
                split2 = arrowSplit[0].split(" AND ")
                instructions.append((2, split2[0], split2[1], arrowSplit[1]))
while instructions:
    newInstructions = instructions.copy()
    for i, instruction in enumerate(instructions):
        wireA = wires.setdefault(instruction[1], -1)
        wireB = wires.setdefault(instruction[2], -1)
        if wireA == -1 or wireB == -1:
            continue
        if instruction[0] == 0:
            if wireA != wireB:
                wires[instruction[3]] = 1
            else:
                wires[instruction[3]] = 0
        elif instruction[0] == 1:
            if wireA == 1 or wireB == 1:
                wires[instruction[3]] = 1
            else:
                wires[instruction[3]] = 0
        elif instruction[0] == 2:
            if wireA == 1 and wireB == 1:
                wires[instruction[3]] = 1
            else:
                wires[instruction[3]] = 0
        newInstructions.remove(instruction)
    instructions = newInstructions.copy()
answerString = ""
wireList = list(wires)
tempList = wireList.copy()
for w in wireList:
    if not w[1:].isdigit():
        tempList.remove(w)
wireList = tempList
def Sort(a):
    return int(a[1:])
wireList.sort(key=Sort, reverse=True)
for w in wireList:
    if w[0] == "z":
        print(wires[w])
        answerString += str(wires[w])
print(answerString)
print(int(answerString, 2))