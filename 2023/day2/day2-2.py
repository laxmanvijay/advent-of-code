from operator import mul
from functools import reduce

with open("input.txt", "r") as f:
    lines = f.readlines()

    possibleGames = []

    for idx, line in enumerate(lines):
        groups = line.split(":")[1].split("; ")

        
        m = {"red": 0, "green": 0, "blue": 0}
        for g in groups:
            colors = g.split(", ")
            
            for c in colors:
                a, b = c.split()

                m[b] = max(m[b], int(a))

        possibleGames.append(reduce(mul, list(m.values())))
    
    print(sum(possibleGames))