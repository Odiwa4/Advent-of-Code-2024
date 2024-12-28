import os
path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"day-3 input.txt")

finalValue = 0

with open (path, 'r') as input:
    lines = input.readlines()
    allLines = "".join(lines)
    test = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    multList = allLines.strip().split("mul(")
    
    enabled = True
    for i in range(len(multList)):
        if (multList[i].find(")") != -1):
            beforeBracket = multList[i].split(")")[0]
            charList = list(beforeBracket)
            fullCharList = list(multList[i])
            hasComma = False
            leftString = ""
            rightString = ""

            valid = True
            lastRightPos = 500
            for x in range(len(charList)):
                if charList[x] == ",":
                    hasComma = True
                if (not hasComma and charList[x].isdigit()):
                    leftString += charList[x]
                elif (hasComma and charList[x].isdigit()):
                    rightString += charList[x]
                    lastRightPos = x
                else:
                    if (x > lastRightPos and fullCharList[x] != ")"):
                        valid = False
            
            doPos = multList[i].rfind("do()")
            dontPos = multList[i].rfind("don't()")
            
            if (valid == True and enabled == True and leftString != "" and leftString.isdigit() and rightString != "" and rightString.isdigit()):
                finalValue += int(leftString) * int(rightString)
                        
            if (doPos != -1 or dontPos != -1):
                enabled = True if doPos > dontPos else False
    input.close()
    print(finalValue)