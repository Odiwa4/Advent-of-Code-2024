import os
path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"Tday-6 input.txt")

board = []
startPos = (-1, -1)
#0 = up, 1 = right, 2 = down, 3 = left
positions = []
obstaclePos = []
direction = 0
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

with open (path, 'r') as d:
    lines = d.readlines()
    for y in range(len(lines)):
        board.append(list(lines[y].strip()))
        for x in range(len (board[y])):
            if (board[y][x] == "^"):
                startPos = (y, x)
            if (board[y][x] == "#"):
                obstaclePos.append((y, x))
    d.close()

def Move(pos):
    stopped = False
    steps = 1
    currentPos = pos

    while stopped == False:
        try:
            nextPos = (currentPos[0]+(directions[direction][0] * steps), currentPos[1]+(directions[direction][1] * steps),)
            if (nextPos[0] < 0 or nextPos[1] < 0):
                steps -= 1
                return[(-1, -1), steps, True]
            elif (board[nextPos[0]][nextPos[1]] == "#"):
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
lastPos = startPos

moves = 0
while found == False:
    moves += 1
    moveAttempt = Move(lastPos)
    if (moveAttempt[2] == True):
        found = True 
    else:
        lastPos = moveAttempt[0]
        if (direction == 3):
            direction = 0
        else:
            direction += 1
            
print(moves)
if (startPos not in positions):
    positions.append(startPos)
    
print(len(positions))
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