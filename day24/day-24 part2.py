'''
My solution for this day was to just make a graph, find where it looks weird and
get my answer semi manually.

P.S. you need the graphviz python library installed plus the graphviz exe then lose your mind
manually checking each and every gate in the generated graph.
'''

import os
import graphviz
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Tday-24 input.txt")
wires = {}
#has tuples, (type, input1, input2, output)
dot = graphviz.Digraph()
instructions = []
nodes = []
connections = []
with open(path, 'r') as d:
    lines = d.readlines()
    for l, line in enumerate(lines):
        if ": " in line:
            splitLine = line.strip().split(": ")
            wires[splitLine[0]] = int(splitLine[1])
        elif " -> " in line:
            arrowSplit = line.strip().split(" -> ")
            instructionNode = ""
            if "XOR" in line:
                split2 = arrowSplit[0].split(" XOR ")
                instructions.append((0, split2[0], split2[1], arrowSplit[1]))
                instructionNode = f"{split2[0]} XOR {split2[1]} TO {arrowSplit[1]}"
            elif "OR" in line:
                split2 = arrowSplit[0].split(" OR ")
                instructions.append((1, split2[0], split2[1], arrowSplit[1]))
                instructionNode = f"{split2[0]} OR {split2[1]} TO {arrowSplit[1]}"
            elif "AND" in line:
                split2 = arrowSplit[0].split(" AND ")
                instructions.append((2, split2[0], split2[1], arrowSplit[1]))
                instructionNode = f"{split2[0]} AND {split2[1]} TO {arrowSplit[1]}"
            #in order, x, y, z
            if instructionNode not in nodes:
                nodes.append(instructionNode)
            if split2[0] not in nodes:
                nodes.append(split2[0])
            if split2[1] not in nodes:
                nodes.append(split2[1])
            if arrowSplit[1] not in nodes:
                nodes.append(arrowSplit[1])
            if (split2[0], instructionNode) not in connections:
                connections.append((split2[0], instructionNode))
            if (split2[1], instructionNode) not in connections:
                connections.append((split2[1], instructionNode))
            if (instructionNode, arrowSplit[1]) not in connections:
                connections.append((instructionNode, arrowSplit[1]))

'''for i, instruction in enumerate(instructions):
    type = instruction[0]
    x = instruction[1]
    y = instruction[2]
    z = instruction[3]

    for i2, instruction2 in enumerate(instructions):
        if i == i2:
            continue
        x2 = instruction2[1]
        y2 = instruction2[2]
        z2 = instruction2[3]'''
correctAnswer = ""
xString = ""
yString = ""
for w in wires:
    if "x" in w:
        xString += str(wires[w])
    elif "y" in w:
        yString += str(wires[w])
correctAnswer = int(xString[::-1], 2) + int(yString[::-1], 2)

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
answerthing = (xString[::-1]+yString[::-1])[::-1]
for w in wireList:
    if w[0] == "z":
        print(wires[w], w)
        answerString += str(wires[w])
print(correctAnswer)
print(bin(correctAnswer)[2:])
print(answerString)
print(int(answerString, 2))

lNodes = nodes
lConnections = connections
nodeList = []
linkList = []

for n, node in enumerate(lNodes):
    if "TO" in node:
        if "XOR" in node:
            dot.node(node, "XOR", shape='box')
        elif "OR" in node:
            dot.node(node, "OR", shape='box')
        elif "AND" in node:
            dot.node(node, "AND", shape='box')
    else:
        dot.node(node)

def GetNode(string):
    for i in nodeList:
        if i.id == string.replace(" ", "_").lower():
            return i
for c in lConnections:
    dot.edge(c[0],c[1])

dot.render('test', view=True)


