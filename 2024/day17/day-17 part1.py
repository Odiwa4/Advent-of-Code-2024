import os
from math import floor

path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"day-17 input.txt")

class Computer:
    def __init__(self, registerA, registerB, registerC, instructions, instructionString):
        self.A = registerA
        self.B = registerB
        self.C = registerC
        self.instructions = instructions
        self.instructionString = instructionString
        self.output = ""

    def __repr__(self):
        return f"A: {self.A} B: {self.B} C: {self.C} I: {self.instructions}"

computer = Computer(0, 0, 0, (0, 0), "")

with open (path, 'r') as d:
    lines = d.readlines()
    A = 0
    B = 0
    C = 0
    instructions = []
    instructionString = ""
    for l, line in enumerate(lines):
        if line.find("Register A") != -1:
            A = int(line.split("Register A: ")[1])
        elif line.find("Register B") != -1:
            B = int(line.split("Register B: ")[1])
        elif line.find("Register C") != -1:
            C = int(line.split("Register C: ")[1])
        elif line.find("Program: ") != -1:
            instructionSplit = line.split("Program: ")[1].split(",")
            temp = 0
            instructions = []
            instructionString = []
            for i, instruction in enumerate(instructionSplit):
                instructionString.append(int(instruction))
                if i % 2 == 0:
                    temp = int(instruction)
                else:
                    instructions.append((temp, int(instruction)))
        computer = Computer(A, B, C, instructions, instructionString)

def GetComboOperand(comp, literalOperand):
    if literalOperand <= 3: return literalOperand
    elif literalOperand == 4: return comp.A
    elif literalOperand == 5: return comp.B
    elif literalOperand == 6: return comp.C
    elif literalOperand == 7: print("fix the bug idiot")
    return -1

def RunInstruction(comp):
    newComp = comp
    instructions = newComp.instructions
    i = 0
    while i < len(instructions):
        instruction = instructions[i]
        opcode = instruction[0]
        operand = instruction[1]
        comboOperand = -1
        if operand != 7: comboOperand = GetComboOperand(comp, operand)

        if opcode == 0:
            try:
                newComp.A = newComp.A // pow(2, comboOperand)
            except ZeroDivisionError:
                newComp.A = 0
        elif opcode == 1:
            newComp.B = newComp.B ^ operand
        elif opcode == 2:
            newComp.B = comboOperand % 8
        elif opcode == 3:
            if newComp.A != 0:
                i = operand
                continue
        elif opcode == 4:
            newComp.B = newComp.B ^ newComp.C
        elif opcode == 5:
            if newComp.output != "":
                newComp.output += ","
            newComp.output += str(comboOperand % 8)
        elif opcode == 6:
            try:
                newComp.B = newComp.A // pow(2, comboOperand)
            except ZeroDivisionError:
                newComp.B = 0
        elif opcode == 7:
            try:
                newComp.C = newComp.A // pow(2, comboOperand)
            except ZeroDivisionError:
                newComp.C = 0
        i+=1
    return newComp

#print(RunInstruction (computer).output)
def GetOutput(comp):
    newComp = comp
    instructions = newComp.instructions
    i = 0
    currentOutput = []
    while i < len(instructions):
        instruction = instructions[i]
        opcode = instruction[0]
        operand = instruction[1]
        comboOperand = -1
        if operand != 7: comboOperand = GetComboOperand(comp, operand)

        if opcode == 0:
            try:
                newComp.A = newComp.A // pow(2, comboOperand)
            except ZeroDivisionError:
                newComp.A = 0
        elif opcode == 1:
            newComp.B = newComp.B ^ operand
        elif opcode == 2:
            newComp.B = comboOperand % 8
        elif opcode == 3:
            if newComp.A != 0:
                i = operand
                continue
        elif opcode == 4:
            newComp.B = newComp.B ^ newComp.C
        elif opcode == 5:
            currentOutput.append(comboOperand % 8)
        elif opcode == 6:
            try:
                newComp.B = newComp.A // pow(2, comboOperand)
            except ZeroDivisionError:
                newComp.B = 0
        elif opcode == 7:
            try:
                newComp.C = newComp.A // pow(2, comboOperand)
            except ZeroDivisionError:
                newComp.C = 0
        i+=1
    return currentOutput
'''for x in range(4097):
    computer.A = x

    computer.output = ""
    print(x, RunInstruction(computer).output)'''

queue = [(15, 0)]
potentialAs = []
#not original but i was out of ideas
while queue:
    index, aValue = queue.pop()
    if index < 0:
        continue
    for o in range(8):
        testA = (aValue << 3) + o

        targetOutput = computer.instructionString[index:]

        tempComp = computer
        tempComp.A = testA
        output = GetOutput(tempComp)

        if not output == targetOutput:
            continue
        if index == 0:
            potentialAs.append(testA)
        queue.append((index-1, testA))

potentialAs.sort()
answer = potentialAs[0]
print(answer)