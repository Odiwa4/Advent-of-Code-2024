import os
import colored
path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"day-16 input.txt")

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

class Path:
    def __init__(self, tiles, currentDirection, cost):
        #current tiles its travelled so far
        self.tiles = tiles
        self.currentDirection = currentDirection
        #the cost so far
        self.cost = cost
        # if it failed / moved backwards
        self.failed = False
        # if its finished
        self.finished = False
        self.consideredPaths = []

    def __repr__(self):
        return f"COST: {self.cost}, TILES: {self.tiles}, CURRENT DIRECTION: {self.currentDirection}, FAILED: {self.failed}"
    def __eq__(self, other):
        if isinstance(other, Path):
            #if self.currentDirection == other.currentDirection and self.tiles[len(self.tiles)-1] == other.tiles[len(other.tiles)-1]:
                #print(other.currentDirection, other.tiles)
            return self.currentDirection == other.currentDirection and self.tiles == other.tiles
        return False

def AddTuple (a, b):
    return (a[0] + b[0], a[1] + b[1])

possiblePaths = []
testedPaths = []

def GetPathCost(path):
    #print(f"{len(testedPaths)} / {len(possiblePaths)}")
    #four rules:
    #for every tile we move to, 1 point
    #if it's a 90-degree turn, 1000 points (plus the one from the last rule)
    #we start north (and add 1k points due to originally being east)
    #if we are forced to retrace, ditch the path
    currentPath = path
    while not currentPath.failed or not currentPath.finished:
        costs = []
        for d in directions:
            currentTile = currentPath.tiles[len(currentPath.tiles)-1]
            tileToCheckPos = AddTuple(currentTile, d)
            tileToCheck = board[tileToCheckPos[1]][tileToCheckPos[0]]
            #check if wall
            if tileToCheck != "#":
                #check if same direction
                if d == currentPath.currentDirection:
                    if tileToCheckPos in currentPath.tiles:
                        costs.append(-1)
                    else:
                        costs.append(1)
                        if tileToCheck == "E":
                            currentPath.cost += 1
                            currentPath.finished = True
                            testedPaths.append(currentPath)
                            return currentPath
                else:
                    #check if already visited
                    if tileToCheckPos in currentPath.tiles:
                        costs.append(-1)
                    else:
                        costs.append(1001)
                        if tileToCheck == "E":
                            currentPath.cost += 1001
                            currentPath.finished = True
                            testedPaths.append(currentPath)
                            return currentPath
            else:
                costs.append(-1)
        #if all of them are walls or backtracking, fail
        if costs == [-1, -1, -1, -1]:
            currentPath.failed = True
            testedPaths.append(currentPath)
            return currentPath
        else:
            lowestCost = 100000
            lowestCostDirection = (0, 0)
            lowestCostIndex = -1
            #find the lowest cost (janky code ahead warning)
            for c in range(len(costs)):
                if costs[c] != -1 and costs[c] < lowestCost:
                    lowestCost = costs[c]
                    lowestCostDirection = directions[c]
                    lowestCostIndex = c

            print(currentPath.cost)
            for c, cost in enumerate(costs):
                if c != lowestCostIndex and cost != -1:
                    currentPath.consideredPaths.append(AddTuple(currentPath.tiles[len(currentPath.tiles)-1], directions[c]))
                    tempTiles = currentPath.tiles.copy()
                    tempTiles.append(AddTuple(currentPath.tiles[len(currentPath.tiles)-1], directions[c]))
                    if Path(tempTiles, directions[c], currentPath.cost + cost) not in testedPaths:
                        possiblePaths.append(Path(tempTiles, directions[c], currentPath.cost + cost))
                        #print(len(tempTiles))
                        GetPathCost(Path(tempTiles, directions[c], currentPath.cost + cost))
                    #else:
                        #print("ahhh")
            currentPath.tiles.append(AddTuple(currentPath.tiles[len(currentPath.tiles)-1], lowestCostDirection))
            currentPath.cost += lowestCost
            currentPath.currentDirection = lowestCostDirection
            #then make new paths for everything that wasnt the lowest

testPath = Path([startPos], (0, -1), 1000)
GetPathCost(testPath)

lowestScore = 5000000000
lowestPath = Path([startPos], (0, -1), 1000)
if len(testedPaths) - 1 == len(possiblePaths):
    for p, path in enumerate(testedPaths):
        if path.failed == False and path.finished == True and path.cost < lowestScore:
            lowestScore = path.cost
            lowestPath = path
    print(lowestScore, len(testedPaths))

for y, line in enumerate(board):
    for x, char in enumerate(board[y]):
        if (x, y) in lowestPath.tiles:
            if (x, y) == startPos:
                print(colored.fore_rgb(0, 255, 0)+ char + "\033[0m", end="")
            else:
                print(colored.fore_rgb(0, 255, 0) + "O" + "\033[0m", end="")

        elif (x, y) in lowestPath.consideredPaths:
            print(colored.fore_rgb(255, 255, 0) + "?" + "\033[0m", end="")
        else:
            print(char, end="")
    print("")
print(len(testedPaths))