import os
path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"day-14 input.txt")

width = 101
height = 103

def MoveRobot(position, velocity, id):
    usingPos = position
    
    for i in range(100):
        currentPos = [usingPos[0] + velocity[0], usingPos[1] + velocity[1]]
        newPos = [-1,-1]
        if currentPos[0] >= width:
            newPos[0] = currentPos[0] - width
        elif currentPos[0] < 0:
            newPos[0] = width + currentPos[0]
        else:
            newPos[0] = currentPos[0]
            
        if currentPos[1] >= height:
            newPos[1] = currentPos[1] - height
        elif currentPos[1] < 0:
            newPos[1] = height + currentPos[1]
        else:
            newPos[1] = currentPos[1]
        
        #print(id, i, "X", currentPos[0], newPos[0])
        #print(id, i, "Y", currentPos[1], newPos[1])
        usingPos = newPos

    return newPos[0], newPos[1]

def GetPositions(position, velocity):
    usingPos = position
    positions = []
    for i in range(10000):
        currentPos = [usingPos[0] + velocity[0], usingPos[1] + velocity[1]]
        newPos = [-1,-1]
        if currentPos[0] >= width:
            newPos[0] = currentPos[0] - width
        elif currentPos[0] < 0:
            newPos[0] = width + currentPos[0]
        else:
            newPos[0] = currentPos[0]
            
        if currentPos[1] >= height:
            newPos[1] = currentPos[1] - height
        elif currentPos[1] < 0:
            newPos[1] = height + currentPos[1]
        else:
            newPos[1] = currentPos[1]
        
        #print(id, i, "X", currentPos[0], newPos[0])
        #print(id, i, "Y", currentPos[1], newPos[1])
        positions.append(newPos)
        usingPos = newPos
        
    return positions
def GetQuadrant(x, y):
    middleWidth = int(((width + 1) / 2))
    middleHeight = int(((height + 1) / 2))
    horizontalHalf = -1
    verticalHalf = -1
    if x < middleWidth - 1:
        horizontalHalf = 1
    elif x > middleWidth - 1:
        horizontalHalf = 2
    
    if y < middleHeight - 1:
        verticalHalf = 1
    elif y > middleHeight - 1:
        verticalHalf = 2
        
    if horizontalHalf == 1 and verticalHalf == 1:
        return 0
    elif horizontalHalf == 2 and verticalHalf == 1:
        return 1
    elif horizontalHalf == 1 and verticalHalf == 2:
        return 2
    elif horizontalHalf == 2 and verticalHalf == 2:
        return 3
    elif horizontalHalf == -1 or verticalHalf == -1:
        return -1
        
class Robot:
    def __init__(self, position, velocity, id):
        self.position = MoveRobot(position, velocity, id)
        self.positions = GetPositions(position, velocity)
        self.velocity = velocity
        self.id = id
        self.quadrant = GetQuadrant(self.position[0], self.position[1])
    def __repr__(self):
        return f'Robot({self.position},{self.velocity})'
robots = []
with open (path, 'r') as d:
    lines = d.readlines()

    for i in range(len(lines)):
        splitLine = lines[i].strip().split(" v=")
        position = splitLine[0].split("p="[1])[1].split(",")
        velocity = splitLine[1].split(",")
        position = list(map(int, position))
        velocity = list(map(int, velocity))
        robots.append(Robot((position[0],position[1]), (velocity[0], velocity[1]), i))

quadrants = {}
for i in range(len(robots)):
    if robots[i].quadrant != -1:
        quadrants.setdefault(robots[i].quadrant, 0)
        quadrants[robots[i].quadrant] += 1

answer = 0
for i in quadrants:
    if answer == 0:
        answer = quadrants[i]
    else:
        answer = answer * quadrants[i]
    
print(answer)

path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"day-14 answer.txt")

blankBoard = []
for i in range(height):
    tempList = []
    for x in range(width):
        tempList.append(" ")
    blankBoard.append(tempList)

with open(path, 'w') as d:
    d.write("")
    d.close()
    
import copy
from PIL import Image, ImageDraw, ImageFont
filePath = os.path.dirname(os.path.abspath(__file__))
for i in range(10000):
    image = Image.new("RGB", (width, height), "white")
    board = copy.deepcopy(blankBoard)
    for r in robots:
        currentPos = r.positions[i]
        image.putpixel((currentPos[0],currentPos[1]), (int((((currentPos[1] + 1) / height) * 255)), int(((currentPos[0] + 1) / width) * 255), int(255 - (((currentPos[1] + 1) / height) * 255))))
    image.save(os.path.join(filePath, f"images/{i+1}.png"))