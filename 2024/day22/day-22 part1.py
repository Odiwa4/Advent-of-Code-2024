import os
import time
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "day-22 input.txt")
secretNumbers = []
with open(path, 'r') as d:
    lines = d.readlines()
    for y, line in enumerate(lines):
        secretNumbers.append(int(line.strip()))

answer = 0
secretNumberIterations = []
for s, secret in enumerate(secretNumbers):
    num = secret
    secretNumberIterations.append([num])
    for i in range(0, 2000):
        num = ((num * 64) ^ num) % 16777216
        num = ((num // 32) ^ num) % 16777216
        num = ((num * 2048) ^ num) % 16777216
        secretNumberIterations[s].append(num)
    print(f"{s+1}/{len(secretNumbers)}")
    answer += num

sequences = {}
startTime = time.perf_counter()
for l, secretList in enumerate(secretNumberIterations):
    combinations = []
    localSequences = {}
    for s, secret in enumerate(secretList):
        if s == 0:
            #gets a starting combination thats ignored
            combinations.append(-50)
            continue
        previousDigit = int(list(str(secretList[s-1]))[len(list(str(secretList[s-1])))-1])
        currentDigit = int(list(str(secret))[len(list(str(secret))) - 1])
        combinations.append(currentDigit - previousDigit)
        if s > 3:
            combinationList = (combinations[s-3], combinations[s-2], combinations[s-1], combinations[s])
            if combinationList not in localSequences:
                localSequences.setdefault(combinationList, 0)
                localSequences[combinationList] = currentDigit
    for i in localSequences:
        sequences.setdefault(i, 0)
        sequences[i] += localSequences[i]
beforeSortedTime = time.perf_counter()
print(max(sequences.values()))
print(len(sequences))
endTime = time.perf_counter()
timeOne = beforeSortedTime - startTime
timeTwo = endTime - startTime
print(f"Time Before Sort: {timeOne:.6f}")
print(f"Final Time: {timeTwo:.6f}")