import os
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "day-25 input.txt")
currentKeyIndex = 0
locks = []
keys = []
lockHeights = []
keyHeights = []
with open(path, 'r') as d:
    lines = d.readlines()
    currentThing = []
    for l, line in enumerate(lines):
        if line.strip() == "":
            currentKeyIndex = l
            if currentThing[0][0] == "#":
                locks.append(currentThing)
            else:
                keys.append(currentThing)
            currentThing = []
        else:
            currentThing.append(lines[l].strip())
    if currentThing[0][0] == "#":
        locks.append(currentThing)
    else:
        keys.append(currentThing)

for k, key in enumerate(keys):
    heights = [-1, -1, -1, -1, -1]
    for m, line in enumerate(key):
        for c, char in enumerate(line):
            if heights[c] == -1 and char == "#":
                heights[c] = m
    keyHeights.append(heights)

for l, lock in enumerate(locks):
    heights = [-1, -1, -1, -1, -1]
    for m in range(len(lock)-1, -1, -1):
        line = lock[m]
        for c, char in enumerate(line):
            if heights[c] == -1 and char == "#":
                heights[c] = m
    lockHeights.append(heights)

answer = 0
for kh, keyHeight in enumerate(keyHeights):
    for lh, lockHeight in enumerate(lockHeights):
        passed = True
        for h in range(len(keyHeight)):
            if lockHeight[h] >= keyHeight[h]:
                passed = False
        if passed:
            answer+=1
print(answer)