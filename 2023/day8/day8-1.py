def readFile():
    with open("2023/day8/input.txt", "r") as f:
        lines = f.readlines()

        directions = lines[0].strip()

        directionsMap = {}

        for line in lines[2:]:
            directionsMap[line.split("=")[0].strip()] = line.split("=")[1].strip().replace("(", "").replace(")", "").replace(" ", "").split(",")
        
        return directions, directionsMap
    
directions, directionsMap = readFile()

current = "AAA"
count = 0


while current != "ZZZ":
    t = 0

    while t <= len(directions) - 1:
        if directions[t] == "R":
            current = directionsMap[current][1]
        elif directions[t] == "L":
            current = directionsMap[current][0]
        t += 1

    count += 1

print(count * len(directions))