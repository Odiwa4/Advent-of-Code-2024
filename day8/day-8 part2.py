import os
path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"day-8 input.txt")
board = []
antennas = {}
with open (path, 'r') as d:
    lines = d.readlines()
    for l in range(len(lines)):
        line = lines[l]
        board.append(list(line.strip()))
    
    for y in range(len(board)):
        for x in range(len(board[y])):
            if (board[y][x] != "."):
                if (board[y][x] not in antennas):
                    antennas[board[y][x]] = []
                antennas[board[y][x]].append((y, x))
    d.close()
    
def PlaceAntinodes(positions, currentAntinodes):
    antinodes = []
    for a in range(len(positions)):
        for b in range(len(positions)):
            try:
                if (positions[a] == positions[b]):
                    continue
                difference = (positions[a][0] - positions[b][0], positions[a][1] - positions[b][1])
                step = 1
                done = False
                while done == False:
                    antinodePos = ((difference[0] * step) + positions[a][0],(difference[1] * step) + positions[a][1])
                    if (antinodePos[0] >= 0 and antinodePos[0] < len(board) and antinodePos[1] >= 0 and antinodePos[1] < len(board[0])):
                        if (antinodePos not in currentAntinodes and antinodePos not in antinodes):
                            antinodes.append(antinodePos)
                        step+=1
                    else:
                        done = True
                        continue
            except IndexError:
                continue
    return antinodes

foundAntinodes = []

for i in antennas.keys():
    foundAntinodes += PlaceAntinodes(antennas[i], foundAntinodes)
    for y in antennas[i]:
        if (y not in foundAntinodes):
            foundAntinodes.append(y)

foundAntinodes = list(dict.fromkeys(foundAntinodes.copy()))


        
print(foundAntinodes)
print(len(foundAntinodes))
