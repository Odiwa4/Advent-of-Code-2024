'''
If anyone is reading this, which (lets be honest) they aren't.
This solution is not original, this problem was difficult, and
once you've looked up the solution in the same language well,
its hard not to just remake their code I guess,

anyway
credit goes to:
https://github.com/hyperneutrino/advent-of-code/blob/main/2024/day21p2.py
for the much smarter solution then the mess I tried before.

also I forgot to include them in day 16, but I used a similar solution by them as well
'''
import os
from collections import deque
from functools import cache
from itertools import product

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "day-21 input.txt")
instructions = []
with open(path, 'r') as d:
    lines = d.readlines()
    for y, line in enumerate(lines):
        instructions.append(line.strip())

#up left down right
directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
dirString = ["^", "<", "v", ">"]
def AddTuple(a, b): return (a[0]+b[0],a[1]+b[1])
def InRange(pos, keypad): return 0 <= pos[0] < len(keypad[0]) and 0 <= pos[1] < len(keypad)
def ComputeSequences(keypad):
    positions = {}
    for y in range(len(keypad)):
        for x in range(len(keypad[y])):
            if keypad[y][x] is not None: positions[keypad[y][x]] = (x,y)
    seqs = {}
    for posA in positions:
        for posB in positions:
            if posA == posB:
                seqs[(posA, posB)] = ["A"]
                continue
            possibilities = []
            queue = deque([(positions[posA], "")])
            optimal = float("inf")
            while queue:
                pos, moves = queue.popleft()
                for d, direction in enumerate(directions):
                    newPos = AddTuple(pos, direction)
                    newChar = dirString[d]
                    if not InRange(newPos, keypad): continue
                    if keypad[newPos[1]][newPos[0]] is None: continue
                    if keypad[newPos[1]][newPos[0]] == posB:
                        if optimal < len(moves) + 1: break
                        optimal = len(moves) + 1
                        possibilities.append(moves + newChar + "A")
                    else:
                        queue.append((newPos, moves + newChar))
                else:
                    continue
                break
            seqs[(posA, posB)] = possibilities
    return seqs

def solve(string, seqs):
    options = [seqs[(posA, posB)] for posA, posB in zip("A" + string, string)]
    return ["".join(posA) for posA in product(*options)]

numKeypad = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    [None,"0", "A"]
]

numSeqs = ComputeSequences(numKeypad)

dirKeypad = [
    [None,"^", "A"],
    ["<", "v", ">"]
]

dirSeqs = ComputeSequences(dirKeypad)
dirLengths = {key: len(value[0]) for key, value in dirSeqs.items()}

@cache
def ComputeLength(seq, depth=25):
    if depth == 1:
        return sum(dirLengths[(posA, posB)] for posA, posB in zip("A" + seq, seq))
    length = 0
    for posA, posB in zip("A" + seq, seq):
        length += min(ComputeLength(subseq, depth - 1) for subseq in dirSeqs[(posA, posB)])
    return length

total = 0

for instruction in instructions:
    inputs = solve(instruction, numSeqs)
    length = min(map(ComputeLength, inputs))
    total += length * int(instruction[:-1])

print(total)