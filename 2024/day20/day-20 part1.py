import os
import heapq
import time
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "day-20 input.txt")
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
def FindCheatLocations(walls):
    queue = [(0, startPos, 0)]
    visited = set()
    cheatLocations = []
    while queue:
        state = heapq.heappop(queue)
        cost, pos, direc = state
        if pos == endPos: return cheatLocations

        if pos in visited: continue
        else: visited.add(pos)

        for d, newDir in enumerate(directions):
            newPos = AddTuple(pos, newDir)
            if newPos in walls:
                testPos = AddTuple(newPos, newDir)
                if testPos not in visited and testPos not in walls and IsInRange(testPos):
                    if newPos not in cheatLocations:
                        cheatLocations.append(newPos)
                continue
            if 0 <= newPos[0] <= width and 0 <= newPos[1] <= height:
                heapq.heappush(queue, (cost+1, newPos, d))

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

defaultScore = TestMap(wallTiles)
cheatSpots = FindCheatLocations(wallTiles)

answer = 0
cheats = 0
startTime = time.perf_counter()
for c, cheat in enumerate(cheatSpots):
    print(f"{c + 1} / {len(cheatSpots)}")
    walls = wallTiles.copy()
    walls.remove(cheat)
    score = TestMap(walls)
    if defaultScore - score > 0:
        cheats += 1
    if defaultScore - score >= 100:
        answer += 1

endTime = time.perf_counter()
elapsedTime = endTime - startTime
print (f"Time: {elapsedTime:.6f}")
print(cheats)
print(answer)