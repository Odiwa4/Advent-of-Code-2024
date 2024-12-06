import os
path = f"{os.path.join(os.path.dirname(os.path.abspath(__file__)),"day-2 input.txt")}"

reports = []
with open (path, 'r') as d:
    lines = d.readlines()
    
    print(len(lines))
    for i in range(len(lines)):
        reports.append(lines[i].split(" ").split("\n")[0])
    d.close()

print(reports)