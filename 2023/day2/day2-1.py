with open("input.txt", "r") as f:
    lines = f.readlines()

    possibleGames = 0

    for idx, line in enumerate(lines):
        groups = line.split(":")[1].split("; ")

        for g in groups:
            m = {"red": 0, "green": 0, "blue": 0}
            colors = g.split(", ")
            
            for c in colors:
                a, b = c.split()

                m[b] = int(a)
        
            if m["red"] > 12 or m["green"] > 13 or m["blue"] > 14:
                break
        else:
            possibleGames += idx + 1

    
    print(possibleGames)