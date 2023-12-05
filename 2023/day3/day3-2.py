from typing import List
from functools import reduce
import random

def createInput():
    with open("input.txt", "r") as f:
        lines = f.readlines()

        input = []

        for line in lines:
            i=0
            inp = []
            while i < len(line):
                if line[i].isdigit():
                    temp = ""
                    while i < len(line) and line[i].isdigit():
                        temp += line[i]
                        i+=1
                    i-=1

                    d = {"val": temp, "id": str(random.random())}
                    
                    inp += [d] * len(temp)
                elif line[i] == '\n':
                    pass
                else:
                    inp.append(line[i])
                i+=1
            input.append(inp)
    
        return input

def findSurroundingNumbers(input: List[List[str]], i: int, j: int, visited: List[str]):
    dirs = [(i, j-1), (i, j+1), (i-1, j), (i+1, j), (i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)]

    result = []
    for dir in dirs:
        if type(input[dir[0]][dir[1]]) == dict:
            try:
                if visited.index(input[dir[0]][dir[1]].get("id")) > -1:
                    pass
            except:
                result.append(input[dir[0]][dir[1]].get("val"))
                visited.append(input[dir[0]][dir[1]].get("id"))
    
    return result

        
def findCumulativeGearRatio():
    input: List[List[str]] = createInput()
    result = 0
    visited: List[str] = []
    for i in range(0, len(input)):
        for j in range(0, len(input[i])):
            if type(input[i][j]) != dict and '*'.find(input[i][j]) >= 0:
                temp = findSurroundingNumbers(input, i, j, visited)

                if len(temp) == 2:
                    result += int(temp[0]) * int(temp[1])

    return result
                

print(findCumulativeGearRatio())

