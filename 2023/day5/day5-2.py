from typing import List, Tuple

def readTillNewLine(firstLine: str, rangeDict: List[Tuple[int, int, int]], lines: List[str]):
    frst = lines.index(firstLine)

    line = ""
    mappings = []
    while line != '\n':
        line = lines[frst + 1]
        if line != "\n":
            mappings.append(line)
        frst += 1
    
    for m in mappings:
        [d, s, r] = m.split()
        rangeDict.append((int(d), int(s), int(r)))

def getValueInRange(rng: List[Tuple[int, int, int]], v: int):
    for r in rng:
        if r[1] <= v <= r[1]+r[2]:
            return r[0]+(v - r[1])
    return v

with open("2023/day5/input.txt", "r") as f:
    lines = f.readlines()

    seeds = []

    seedsT = list(map(lambda x: int(x), 
                lines[0].split(": ")[1].split()))
    
    for i in range(0, len(seedsT), 2):
        seeds.append(range(seedsT[i], seedsT[i] + seedsT[i+1]))

    print(seeds)

    seedToSoil = []
    soilToFertilizer = []
    fertilizerToWater = []
    waterToLight = []
    lightToTemperature = []
    temperatureToHumidity = []
    humidityToLocation = []

    readTillNewLine("seed-to-soil map:\n", seedToSoil, lines)
    readTillNewLine("soil-to-fertilizer map:\n", soilToFertilizer, lines)
    readTillNewLine("fertilizer-to-water map:\n", fertilizerToWater, lines)
    readTillNewLine("water-to-light map:\n", waterToLight, lines)
    readTillNewLine("light-to-temperature map:\n", lightToTemperature, lines)
    readTillNewLine("temperature-to-humidity map:\n", temperatureToHumidity, lines)
    readTillNewLine("humidity-to-location map:\n", humidityToLocation, lines)

    
    location = []
    for s in seeds:
        for i in s:
            soil = getValueInRange(seedToSoil, i)
            fert = getValueInRange(soilToFertilizer, soil)
            water = getValueInRange(fertilizerToWater, fert)
            light = getValueInRange(waterToLight, water)
            temp = getValueInRange(lightToTemperature, light)
            humid = getValueInRange(temperatureToHumidity, temp)
            loc = getValueInRange(humidityToLocation, humid)

            location.append(loc)
    
    print(min(location))
