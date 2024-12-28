import os
from collections import namedtuple
path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"day-12 input.txt")
tiles = []
searched = []

directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
def GetArea(startPos, letterToFind):
    positions = []
    def FindTiles(position):
        for d in directions:
            currentPos = (position[0] + d[0], position[1] + d[1])
            if (currentPos[1] >= 0 and currentPos[1] < len(tiles[0]) and currentPos[0] >= 0 and currentPos[0] < len(tiles)):
                if (tiles[currentPos[1]][currentPos[0]] == letterToFind and searched[currentPos[1]][currentPos[0]] == False):
                    if (currentPos not in positions):
                        positions.append(currentPos)
                        searched[currentPos[1]][currentPos[0]] = True
                        FindTiles(currentPos)
    
    for d in directions:
        currentPos = (startPos[0] + d[0], startPos[1] + d[1])
        if (currentPos[1] >= 0 and currentPos[1] < len(tiles[0]) and currentPos[0] >= 0 and currentPos[0] < len(tiles)):
            if (tiles[currentPos[1]][currentPos[0]] == letterToFind and searched[currentPos[1]][currentPos[0]] == False):
                positions.append(currentPos)
                searched[currentPos[1]][currentPos[0]] = True
                FindTiles(currentPos)
    
    if (startPos not in positions):
        positions.append(startPos)
    return positions

class PerimeterPiece():
    def __init__(self, direction, position):
        self.direction = direction
        self.position = position
        
    def __eq__(self, other):
        if isinstance(other, PerimeterPiece):
            return self.direction == other.direction and self.position == other.position
        return False

def GetPerimeter(area, letterToFind):
    positions = []
    for i in range(len(area)):
        for d in directions:
            currentPos = (area[i][0] + d[0], area[i][1] + d[1])
            if (currentPos[1] >= 0 and currentPos[1] < len(tiles[0]) and currentPos[0] >= 0 and currentPos[0] < len(tiles)):
                if (tiles[currentPos[1]][currentPos[0]] != letterToFind):
                    positions.append(PerimeterPiece(d, currentPos))
            else:
                positions.append(PerimeterPiece(d, currentPos))

    return positions
def HasPerimeterInList(direc, pos, perimeterlist):
    for i in range(len(perimeterlist)):
        if perimeterlist[i].direction == direc and perimeterlist[i].position == pos:
            return True
        
    return False

def GetSides(perimeter, letterToFind):
    perimeterList = perimeter.copy()
    
    for i in range(len(perimeter)):
        pos = perimeter[i].position
        direc = perimeter[i].direction
        if (perimeter[i] not in perimeterList):
            continue
        canDirection = [True, True]
        step = 1
        while (True in canDirection):
            # can direction is the directions its able to go,
            # it basically removes all the other perimeter list elements in the same side if that makes any sense
            # and we only go the directions we need to
            horizontalDirections = [(-1, 0), (1, 0)]
            verticalDirections = [(0, -1), (0, 1)]
            directionList = []
            if (direc[0] != 0):
                directionList = verticalDirections.copy()
            else:
                directionList = horizontalDirections.copy()
            for x in range(len(directionList)):
                d = directionList[x]
                if (canDirection[x]):
                    currentPos = (pos[0] + (d[0] * step), pos[1] + (d[1] * step))
                    if (PerimeterPiece(direc, currentPos) in perimeterList):
                        perimeterList.remove(PerimeterPiece(direc, currentPos))
                    else:
                        canDirection[x] = False
            step+=1
    
    return perimeterList

class Region():
    def __init__(self, pos):
        self.letter = tiles[pos[1]][pos[0]]
        self.areaArray = GetArea(pos, self.letter)
        self.area = len(self.areaArray)
        self.perimeterArray = GetPerimeter(self.areaArray, self.letter)
        self.perimeter = len(self.perimeterArray)
        self.sidesArray = GetSides(self.perimeterArray, self.letter)
        self.sides = len(self.sidesArray)
        self.costOne = self.area * self.perimeter
        self.costTwo = self.area * self.sides
        
with open (path, 'r') as d:
    lines = d.readlines()

    for y in range(len(lines)):
        tiles.append(list(lines[y].strip()))
        tempList = []
        for x in range(len(lines[y])):
            tempList.append(False)
        searched.append(tempList)
    d.close()

regions = []
for y in range(len(tiles)):
    for x in range(len(tiles[y])):
        if (searched[y][x] == False):
            regions.append(Region((x, y)))

answer = 0
i = 0
for region in regions:
    print(f"{i + 1} / {len(regions)} / {region.sides}")
    answer += region.costTwo
    i += 1
print(region.perimeter)
print(answer)