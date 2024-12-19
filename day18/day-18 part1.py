import os
import heapq
import time
from collections import deque

import colored
path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"day-18 input.txt")

#test = 7, 7, 12
#real, 71, 71, 1024
width = 71
height = 71
lineLimit = 1024
corruptedTiles = []
with open (path, 'r') as d:
    lines = d.readlines()
    for l, line in enumerate(lines):
        splitLine = line.strip().split(",")
        corruptedTiles.append((int(splitLine[0]),int(splitLine[1])))

#up left down right
directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
def AddTuple(a, b):
    return (a[0] + b[0], a[1] + b[1])

def IsInRange(pos):
    return 0 <= pos[0] < width and 0 <= pos[1] < height

currentCorruptedTiles = set(corruptedTiles.copy()[:1024])
validPositions = set((x, y) for x in range(width) for y in range(height))
startTime = time.perf_counter()
for i in range(3451-1024):
    print(f"{i+1024}/{3450+1024}")
    currentCorruptedTiles.add(corruptedTiles[i+1024])
    queue = [(0, (0, 0), 3)]
    seenTiles = set()
    test = 0
    finished = False
    while queue:
        cost, pos, dir = heapq.heappop(queue)

        if pos in seenTiles:
            continue
        else:
            seenTiles.add(pos)

        if pos == (width - 1, height - 1):
            endState = (pos, dir)
            finished = True
            print(cost)
            break

        for newDir in range(len(directions)):
            newPos = AddTuple(pos, directions[newDir])
            newCost = cost + 1
            if newPos in seenTiles or not newPos in validPositions:
                continue
            if newPos in currentCorruptedTiles:
                continue
            heapq.heappush(queue, (newCost, newPos, newDir))
    if not finished:
        endTime = time.perf_counter()
        print(corruptedTiles[i])
        elapsedTime = endTime-startTime
        print (f"Time: {elapsedTime:.6f}")
        break