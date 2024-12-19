import os
import heapq
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

def GetNextDirection(index, offset):
    if offset == -1:
        if index > 0:
            return index - 1
        else:
            return 3
    else:
        if index < 3:
            return index + 1
        else:
            return 0

def IsInRange(pos):
    return 0 <= pos[0] < width and 0 <= pos[1] < height

for i in range(3451):
    print(i)
    currentCorruptedTiles = corruptedTiles[:1024+i]
    print(currentCorruptedTiles[len(currentCorruptedTiles)-1])
    queue = [(0, (0, 0), 3)]
    seenTiles = []
    backtrack = {}
    endState = ((0, 0), (0, 0))
    test = 0
    finished = False
    while queue:
        cost, pos, dir = heapq.heappop(queue)

        if pos in seenTiles:
            continue
        else:
            seenTiles.append(pos)

        if pos == (width - 1, height - 1):
            endState = (pos, dir)
            finished = True
            print(cost)
            break



        for newCost, newPos, newDir in [(cost+1, AddTuple(pos, directions[dir]), dir), (cost+1, AddTuple(pos, directions[GetNextDirection(dir, -1)]), GetNextDirection(dir, -1)), (cost+1, AddTuple(pos, directions[GetNextDirection(dir, 1)]), GetNextDirection(dir, 1))]:
            if IsInRange(newPos):
                if newPos in currentCorruptedTiles:
                    continue
            else:
                continue

            backtrack[(newPos, newDir)] = (pos, dir)
            heapq.heappush(queue, (newCost, newPos, newDir))
    if not finished:
        print(currentCorruptedTiles[len(currentCorruptedTiles)-1])
        break