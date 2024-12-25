import os
leftNum = 0
rightNum = 0
path = f"{os.path.join(os.path.dirname(os.path.abspath(__file__)),"day-1 input.txt")}"
puzzle_input = ""

with open (path, 'r') as d:
    puzzle_input = d.read()
    d.close()

from collections import defaultdict

def part2():
    first = defaultdict(int)
    second = defaultdict(int)
    for line in puzzle_input.split('\n'):
        a, b = map(int, line.split())
        first[a] += 1
        second[b] += 1

    similarity = 0
    for num, count in first.items():
        similarity += num * count * second[num]

    return similarity
print(part2())
