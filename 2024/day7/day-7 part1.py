import os
import time
from collections import namedtuple
path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"day-7 input.txt")
calibrations = []

class Calibration:
    result = 0
    inputs = []
    def __init__(self, newResults, newInputs):
        self.result = newResults
        self.inputs = newInputs 
        
with open (path, 'r') as d:
    lines = d.readlines()
    for l in range(len(lines)):
        line = lines[l]
        lineSplit = line.split(": ")
        result = int(lineSplit[0])
        inputs = list(map(int, (lineSplit[1].strip("\n").split(" "))))
        calibrations.append(Calibration(result, inputs))
    d.close()

def GetBinaryString(length):
    bitMax = 2**(length)
    binary = []
    for i in range(bitMax):
        tempList = list(bin(i)[2:].zfill(length))
        tempList = list(map(int, tempList))
        binary.append(tempList)

    return binary

def BruteForce(calibration):
    result = calibration.result
    inputs = calibration.inputs
    equations = GetBinaryString(len(inputs)-1)
    #EQUATIONS = 00, 01, 10, 11
    for x in range(len(equations)):
        tested = False
        currentEquations = equations[x].copy()
        currentInputs = inputs.copy()
        while tested == False:
            #INPUTS = 52, 22, 14
                num = 0
                if (currentEquations[0] == 0):
                    num = currentInputs[0] + currentInputs[1]
                elif (currentEquations[0] == 1):
                    num = currentInputs[0] * currentInputs[1]
                    
                tempInputs = []
                tempEquations = []

                if (len(currentInputs) > 2):
                    for i in range(len(currentInputs)):
                        if i == 0:
                            tempInputs.append(num)
                            continue
                        elif i == len(currentInputs) - 1:
                            break
                        else:
                            tempInputs.append(currentInputs[i + 1])
                    currentInputs = tempInputs.copy()
                    for i in range(len(currentEquations)):
                        if i == len(currentEquations) - 1:
                            break
                        else:
                            tempEquations.append(currentEquations[i + 1])
                    currentEquations = tempEquations.copy()
                    
                else:
                    if (num == result):
                        tested = True
                        return True
                    else:
                        tested = True

    return False
   
answer = 0             
for i in range(len(calibrations)):
    print(f"{i + 1} / {len(calibrations)}")
    if (BruteForce(calibrations[i])):
        answer += calibrations[i].result

print(answer)