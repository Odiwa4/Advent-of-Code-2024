import os
path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"day-10 input.txt")
board = []
zeros = []

#use this to switch between parts
part = 2
with open (path, 'r') as d:
    lines = d.readlines()

    for y in range(len(lines)):
        board.append(list(lines[y].strip()))
        board[y] = list(map(int, board[y]))
        for x in range(len(board[y])):
            if (board[y][x] == 0):
                zeros.append((y, x))
    d.close()
    
directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
def FindTrailheadScore(zero):
    score = []
    nines = []
    def FindNeighbours(currentNum, position):
        for d in directions:
            try:
                currentPos = (position[0] + d[0],position[1] + d[1])
                if (currentPos[0] >= 0 and currentPos[0] < len(board) and currentPos[1] >= 0 and currentPos[1] < len(board[0])):
                    if (board[currentPos[0]][currentPos[1]] == currentNum + 1):
                        if (currentNum + 1 == 9):
                            if (part == 1):
                                if (currentPos not in nines):
                                    score.append(1)
                                    nines.append(currentPos)
                            elif (part == 2):
                                score.append(1)
                            continue
                        else:
                            FindNeighbours(currentNum + 1, currentPos)
                else:
                    continue
            except (ValueError,IndexError):
                continue
    for d in directions:
        try:
            if (board[zero[0] + d[0]][zero[1] + d[1]] == 1):
                FindNeighbours(1, (zero[0] + d[0],zero[1] + d[1]))
        except IndexError:
            continue
    return len(score)

sum = 0
for i in range(len(zeros)):
    sum += FindTrailheadScore(zeros[i])
    
print(sum)