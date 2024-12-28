import os
path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"day-4 input.txt")

wordSearch = []
with open (path, 'r') as d:
    lines = d.readlines()

    for i in range(len(lines)):
        wordSearch.append(list(lines[i].strip()))
    d.close()

xCoords = []
yCoords = []

def CheckXMAS(xPos, yPos, xOffset, yOffset):
    
    for i in range(4):  # Length of "XMAS"
        newX = xPos + i * xOffset
        newY = yPos + i * yOffset

        if newY < 0 or newY >= len(wordSearch) or newX < 0 or newX >= len(wordSearch[0]):
            return False

        # Check each letter in sequence
        targetChar = "XMAS"[i]
        if wordSearch[newY][newX] != targetChar:
            return False

    return True

def CheckXMASes(x, y, rotation):
    newX = x
    newY = y
    if newY < 1 or newY >= len(wordSearch) - 1 or newX < 1 or newX >= len(wordSearch[0]) - 1:
        return False
        
    if (rotation == 0):
        if (wordSearch[y+1][x+1] == "M" and wordSearch[y+1][x-1] == "M" and wordSearch[y-1][x+1] == "S" and wordSearch[y-1][x-1] == "S"):
            return True
    elif (rotation == 1):
        if (wordSearch[y+1][x+1] == "S" and wordSearch[y+1][x-1] == "S" and wordSearch[y-1][x+1] == "M" and wordSearch[y-1][x-1] == "M"):
            return True
    elif (rotation == 2):
        if (wordSearch[y+1][x+1] == "M" and wordSearch[y+1][x-1] == "S" and wordSearch[y-1][x+1] == "M" and wordSearch[y-1][x-1] == "S"):
            return True
    elif (rotation == 3):
        if (wordSearch[y+1][x+1] == "S" and wordSearch[y+1][x-1] == "M" and wordSearch[y-1][x+1] == "S" and wordSearch[y-1][x-1] == "M"):
            return True
    return False
def FindXMAS():
    foundXmas = 0
    for y in range(len(wordSearch)):
        for x in range(len(wordSearch[y])):
            if (wordSearch[y][x] == "A"):
                for i in range (4):
                    try:
                        if CheckXMASes(x, y, i):
                            foundXmas += 1
                            xCoords.append(x)
                            yCoords.append(y)
                    except IndexError:
                        pass
    print(xCoords)
    print(yCoords)
    return foundXmas
                
print(FindXMAS())