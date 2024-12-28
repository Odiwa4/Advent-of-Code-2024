import os
from collections import deque
import heapq
import colored
path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"day-16 input.txt")
'''
gonna be honest here, practically none if this code is original its just code from a video
that i copied and slightly changed to fit with my code but at least i know for the future...

sure...
'''
board = []
startPos, endPos = (), ()
# up left down right
directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
with open (path, 'r') as d:
    lines = d.readlines()
    for y in range(len(lines)):
        board.append(list(lines[y].strip("\n")))
        for x in range(len(board[y])):
            if board[y][x] == "S":
                startPos = (x, y)
            elif board[y][x] == "E":
                endPos = (x, y)


def AddTuple(a,b):
    return (a[0] + b[0], a[1] + b[1])

def GetRotDir(index, offset):
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

#cost, location, direction
queue = [(0, startPos, 3)]
lowestCost = {(startPos, 3): 0}
backtrack = {}
bestCost = float("inf")
endStates = set()
while queue:
    cost, position, direction = heapq.heappop(queue)
    if cost > lowestCost.get((position, direction), float("inf")):
        continue

    if position == endPos:
        if cost > bestCost:
            break
        bestCost = cost
        endStates.add((position, direction))

    for newCost, newPosition, newDirection in [(cost+1, AddTuple(position, directions[direction]), direction), (cost+1000, position, GetRotDir(direction, -1)), (cost+1000, position, GetRotDir(direction, 1))]:
        if board[newPosition[1]][newPosition[0]] == "#":
            continue
        lowest = lowestCost.get((newPosition, newDirection), float("inf"))
        if newCost > lowest:
            continue
        if newCost < lowest:
            backtrack[(newPosition, newDirection)] = set()
            lowestCost[(newPosition, newDirection)] = newCost
        backtrack[(newPosition, newDirection)].add((position, direction))

        heapq.heappush(queue, (newCost, newPosition, newDirection))

states = deque(endStates)
seen = set(endStates)

while states:
    key = states.popleft()
    for last in backtrack.get(key, []):
        if last in seen:
            continue
        seen.add(last)
        states.append(last)

tiles = {position for position, direction in seen}
#print(len(tiles))
#print(backtrack)
for y, line in enumerate(board):
    for x, char in enumerate(board[y]):
        if (x, y) in tiles:
            if (x, y) == startPos:
                print(colored.fore_rgb(0, 255, 0)+ char + "\033[0m", end="")
            else:
                print(colored.fore_rgb(0, 255, 0) + "O" + "\033[0m", end="")
        else:
            print(char, end="")
    print("")