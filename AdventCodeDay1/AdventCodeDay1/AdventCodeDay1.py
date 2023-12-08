from re import X
from tkinter import CURRENT


numStr = {
    'one':1,
    'two':2,
    'three':3,
    'four':4,
    'five':5,
    'six':6,
    'seven':7,
    'eight':8,
    'nine':9
    }

with open ("C:\\Users\\thanu\\OneDrive\\Documents\\Advent of Code 2023\\dayone.txt", "r") as data:
    totalNumbers = []
    for line in data:
       ## print(line)
        currentNum = []
        currentstr  = ""
        checked = False

        for x in line:
            if x .isdigit():
                currentNum.append(x)
                currentstr = ""
            else:
                
                currentstr+=x
                ##print(currentstr)

                for key in numStr.keys():
                    currentstrwithprev =  line[line.index(currentstr)-1] +currentstr
                    if key in currentstr or key in currentstrwithprev:
                          currentNum.append(numStr[key])
                          checked = True
                          currentstr = ""
                if checked:
                    currenstr = ""

        print(currentNum)
        totalNumbers.append(int(str(currentNum[0])+str(currentNum[-1])))
    print(totalNumbers)
    print(sum(totalNumbers))
