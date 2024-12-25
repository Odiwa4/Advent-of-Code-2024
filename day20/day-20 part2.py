import os
import heapq
import time
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "day-20 input.txt")
threshold = 100
startPos = ()
endPos = ()
wallTiles = set()

with open(path, 'r') as d:
    lines = d.readlines()
    width = len(lines[0].strip())-1
    height = len(lines)-1
    for y, line in enumerate(lines):
        for x, char in enumerate(line.strip()):
            if char == "#":
                wallTiles.add((x, y))
            elif char == "S":
                startPos = (x, y)
            elif char == "E":
                endPos = (x, y)
directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

def AddTuple(a, b): return (a[0] + b[0], a[1] + b[1])
def MultTuple(a,b): return (a[0]*b,a[1]*b)
def IsInRange(pos): return 0 <= pos[0] <= width and 0 <= pos[1] <= height

def TestMap(walls):
    queue = [(0, startPos)]
    visited = set()
    while queue:
        state = heapq.heappop(queue)
        cost, pos = state
        if pos == endPos: return cost

        if pos in visited: continue
        else: visited.add(pos)

        for d, newDir in enumerate(directions):
            newPos = AddTuple(pos, newDir)
            if not IsInRange(newPos):
                continue
            if newPos in walls:
                continue
            if newPos in visited:
                continue
            heapq.heappush(queue, (cost + 1, newPos))

#test has 285 cheats
def GetCostsAtPositions(walls):
    queue = [(0, startPos)]
    costs = {startPos: 0}
    visited = set()
    while queue:
        state = heapq.heappop(queue)
        cost, pos = state

        if pos in visited: continue
        else:
            visited.add(pos)
            costs[pos] = cost

        if pos == endPos: return costs

        for d, newDir in enumerate(directions):
            newPos = AddTuple(pos, newDir)
            if not IsInRange(newPos):
                continue
            if newPos in walls:
                continue
            if newPos in visited:
                continue
            heapq.heappush(queue, (cost + 1, newPos))
            costs.setdefault(pos, 0)

def GetManhattanDistance(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])
def FindCheats(walls, costDict):
    test = 0
    cheats = set()
    for p, pos in enumerate(costDict):
        if pos == endPos:
            break
        print(f"{p+1} / {len(costDict)-1}")
        for x in range(-20, 21):
            for y in range(-20, 21):
                newPos = AddTuple(pos, (x, y))
                if not IsInRange(newPos):
                    continue
                if newPos in walls:
                    continue
                cost = costDict[pos]
                otherCost = costDict[newPos]
                if cost < otherCost:
                    nonCheatingDistance = otherCost - cost
                    cheatingDistance = GetManhattanDistance(pos, newPos)

                    if cheatingDistance > 20:
                        continue
                    if cheatingDistance < nonCheatingDistance:
                        if (pos, newPos) not in cheats:
                            if nonCheatingDistance - cheatingDistance >= threshold:

                                cheats.add((pos, newPos))
    return cheats

defaultScore = TestMap(wallTiles)

answer = 0
cheats = 0
startTime = time.perf_counter()

print(len(FindCheats(wallTiles, GetCostsAtPositions(wallTiles))))