import os
path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"day-6 input.txt")

board = []
startPos = (-1, -1)
#0 = up, 1 = right, 2 = down, 3 = left
positions = []
obstaclePos = []
newObstanceSpots = []
direction = 0
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

attemptsToFail = 100

with open (path, 'r') as d:
    lines = d.readlines()
    for y in range(len(lines)):
        board.append(list(lines[y].strip()))
        for x in range(len (board[y])):
            if (board[y][x] == "^"):
                startPos = (y, x)
            elif (board[y][x] == "#"):
                obstaclePos.append((y, x))
            else:
                newObstanceSpots.append((y, x))
    d.close()

def Move(pos, currentBoard):
    stopped = False
    steps = 1
    currentPos = pos

    while stopped == False:
        try:
            nextPos = (currentPos[0]+(directions[direction][0] * steps), currentPos[1]+(directions[direction][1] * steps),)
            if (nextPos[0] < 0 or nextPos[1] < 0):
                steps -= 1
                return[(-1, -1), steps, True]
            elif (currentBoard[nextPos[0]][nextPos[1]] == "#"):
                steps -= 1

                oldPos = (currentPos[0]+(directions[direction][0] * steps), currentPos[1]+(directions[direction][1] * steps),)

                stopped = True
                return [oldPos, steps, False]
            else:
                if (nextPos not in positions):
                    positions.append(nextPos)
                steps += 1
        except IndexError:
            steps -= 1
            stopped = True
            return[(-1, -1), steps, True]

found = False


foundObstacles = 0
for o in range(len(newObstanceSpots)):
    print(str(o) + " / " + str(len(newObstanceSpots) - 1))
    currentBoard = board.copy()
    for i in range (len(currentBoard)):
        currentBoard[i] = board[i].copy()
    currentBoard[newObstanceSpots[o][0]][newObstanceSpots[o][1]] = "#"
    lastPos = startPos
    direction = 0
    for a in range(attemptsToFail):
        moveAttempt = Move(lastPos, currentBoard)
        if (moveAttempt[2] == True):
            break
        else:
            lastPos = moveAttempt[0]
            if (direction == 3):
                direction = 0
            else:
                direction += 1
        if (a == attemptsToFail - 1):
            foundObstacles += 1
            
if (startPos not in positions):
    positions.append(startPos)
    
print(foundObstacles)
debugBoard = []
for y in range(len(board)):
    line = ""
    for x in range(len(board[y])):
        if (y, x) == startPos:
            line += "^"
        elif (y, x) in positions:
            line += "~"
        elif (y, x) in obstaclePos:
            line += "#"
        else:
            line += "."
        line += " "
        if (x == len(board[y]) - 1):
            line += "\n"
        
        
    debugBoard.append(line)
    
path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"fileTest.txt")
with open (path, 'w') as d:
    d.writelines(debugBoard)
    d.close()