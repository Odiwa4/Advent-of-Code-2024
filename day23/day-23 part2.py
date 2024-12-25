import os
import time
from collections import deque
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "day-23 input.txt")
connections = {}
startTime = time.perf_counter()
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
def FindGroups():
    foundGroups = set()
    for index, c in enumerate(connections):
        print(f"{index+1}/{len(connections)}")
        queue = deque([[c]])
        while queue:
            currentConnections = queue.popleft()
            if frozenset(currentConnections) in foundGroups: continue
            for p, possibility in enumerate(connections[currentConnections[len(currentConnections)-1]]):
                if possibility in currentConnections: continue
                if not all(possibility in connections[conn] for conn in currentConnections):
                    foundGroups.add(frozenset(currentConnections))
                    break
                else:
                    tempList = currentConnections + [possibility]
                    queue.append(tempList)
                    continue
    return list(foundGroups)
foundGroups = list(FindGroups())
foundGroups = list(map(list, foundGroups))
foundGroups.sort(key=len, reverse=True)
answerList = foundGroups[0]
answerList.sort()
answer = ""
for a, ans in enumerate(answerList):
    if a != 0:
        answer+=","
    answer+=ans
endTime = time.perf_counter()
elapsedTime = endTime - startTime
print(f"Time: {elapsedTime:.6f}")
print(answer)