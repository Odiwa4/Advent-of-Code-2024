import os
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "day-23 input.txt")
groups = set()
connections = {}
with open(path, 'r') as d:
    lines = d.readlines()
    for l, line in enumerate(lines):
        splitLine = line.strip().split("-")
        comp1 = splitLine[0]
        comp2 = splitLine[1]
        connections.setdefault(comp1, [])
        if comp2 not in connections[comp1]:
            connections[comp1].append(comp2)
        connections.setdefault(comp2, [])
        if comp1 not in connections[comp2]:
            connections[comp2].append(comp1)

def CreateGroups():
    for c in connections:
        for p, possibility in enumerate(connections[c]):
            for p2, possibility2 in enumerate(connections[c]):
                if possibility == possibility2: continue
                if c in connections[possibility2] and possibility in connections[possibility2]:
                    tempSet = frozenset([c, possibility, possibility2])
                    if tempSet not in groups:
                        groups.add(tempSet)

def FindTSets():
    answer = 0
    for g, group in enumerate(groups):
        for c, computer in enumerate(group):
            if computer[0] == "t":
                answer+=1
                break
    return answer
CreateGroups()
print(FindTSets())
