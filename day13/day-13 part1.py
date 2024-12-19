import os
import numpy

path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"day-13 input.txt")

class ClawMachine:
    def __init__(self, buttonA, buttonB, prize):
        self.buttonA = buttonA
        self.buttonB = buttonB
        self.prize = prize
    
    def __repr__(self):
        return f'ClawMachine({self.buttonA},{self.buttonB},{self.prize})'
machines = []
with open (path, 'r') as d:
    lines = d.readlines()

    machinePart = 0
    lastButtonA = ()
    lastButtonB = ()
    for y in range(len(lines)):
        if "Button A" in lines[y]:
            machinePart = 1
            tempString = lines[y].strip().split("Button A: ")[1].split(", ")
            lastButtonA = (int(tempString[0].split("X+")[1]), int(tempString[1].split("Y+")[1]))
        elif "Button B" in lines[y]:
            machinePart = 2
            tempString = lines[y].strip().split("Button B: ")[1].split(", ")
            lastButtonB = (int(tempString[0].split("X+")[1]), int(tempString[1].split("Y+")[1]))
        elif "Prize" in lines[y]:
            machinePart = 3
            tempString = lines[y].strip().split("Prize: ")[1].split(", ")
            prize = (int(tempString[0].split("X=")[1]) + 10000000000000, int(tempString[1].split("Y=")[1]) + 10000000000000)
            machines.append(ClawMachine(lastButtonA, lastButtonB, prize))
    d.close()
    
def GetPrize(machine):
    A = numpy.array([[machine.buttonA[0], machine.buttonB[0]],[machine.buttonA[1], machine.buttonB[1]]])
    B = numpy.array([machine.prize[0], machine.prize[1]])
    
    solution = numpy.linalg.solve(A, B)

    def is_almost_integer(value, tol=1e-4):
        return abs(value - round(value)) < tol

    if (is_almost_integer(solution[0]) and is_almost_integer(solution[1])):
        return round(solution[0]) * 3 + round(solution[1])
    else:
        return 0
        
    
answer = 0
for machine in machines:
    print(GetPrize(machine), "result :)")
    answer += GetPrize(machine)

print(len(machines))
print(answer)