import os
import time
path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"day-19 input.txt")
patterns = []
towelsToTry = []
with open (path, 'r') as d:
    lines = d.readlines()
    for l, line in enumerate(lines):
        if l == 0:
            splitLine = line.strip().split(", ")
            for p, pattern in enumerate(splitLine):
                patterns.append((len(pattern), pattern, pattern[0]))
        elif l > 1:
            towelsToTry.append(line.strip())

def GenerateBlankDictionary(len):
    tempDict = {}
    for i in range(len):
        if i == 0: tempDict.setdefault(i, 1)
        else: tempDict.setdefault(i, 0)
    return tempDict
def IsPatternValid(patternString):
    statesToTest = GenerateBlankDictionary(len(patternString))
    success = 0
    for i in statesToTest:
        times = statesToTest.get(i)
        for p, pattern in enumerate(patterns):
            #starts with the same letter
            if pattern[2] != patternString[i]:
                continue
            #and fits
            if len(patternString[i:]) < pattern[0]:
                continue
            currentString = patternString[i:][:pattern[0]]
            if currentString == pattern[1]:
                if i + pattern[0] > len(patternString)-1:
                    success += times
                else:
                    statesToTest[i + pattern[0]] += times
    return success

answer = 0
possible = 0
startTime = time.perf_counter()
for t, towel in enumerate(towelsToTry):
    result = IsPatternValid(towel)
    print(f"{t + 1} / {len(towelsToTry)}: {result}")
    answer+=result
    if result > 0:
        possible += 1
endTime = time.perf_counter()
elapsedTime = endTime-startTime
print(f"Time: {elapsedTime:.6f}")
print(f"Part One: {possible}")
print(f"Part Two: {answer}")