from typing import Dict, List, Tuple
from functools import reduce, cmp_to_key
from collections import Counter

cardRanks = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


def readInput():
    with open("2023/day7/test.txt", "r") as f:
        lines = f.readlines()
        input = []
        for line in lines:
            input.append(line.split())
        
        return input
    

def modifyJ(cardsMap: List[List[str]]):
    respMap: List[List[str]] = []

    for card in cardsMap:
        ctr = Counter([i for i in card[0] if i != 'J'])
        try:
            toReplace = ctr.most_common(1)[0][0]
            temp = card[0].replace("J", toReplace)
            respMap.append([temp, card[1]])
        except:
            respMap.append(card)
    
    return respMap


def ruleParser(cardsMap: List[List[str]]):
    cardsWithTypes: Dict[str, List[List[str]]] = {
        "fiveOfAKind": [],
        "fourOfAKind": [],
        "fullHouse": [],
        "threeOfAKind": [],
        "twoPair": [],
        "onePair": [],
        "highCard": []
    }

    for card in cardsMap:
        hand = card[0]

        if len(set(hand)) == 1: # fiveOfAKind
            cardsWithTypes["fiveOfAKind"].append(card)
        elif len(set(hand)) == 2: # fourOfAKind or fullHouse
            ctr = Counter(hand)
            if ctr.most_common(1)[0][1] == 4: # fourOfAKind
                cardsWithTypes["fourOfAKind"].append(card)
            elif ctr.most_common(1)[0][1] == 3:
                cardsWithTypes["fullHouse"].append(card)
        elif len(set(hand)) == 3: # threeOfAKind or twoPair
            ctr = Counter(hand)
            if ctr.most_common(1)[0][1] == 3: # fourOfAKind
                cardsWithTypes["threeOfAKind"].append(card)
            elif ctr.most_common(1)[0][1] == 2:
                cardsWithTypes["twoPair"].append(card)
        elif len(set(hand)) == 4:
            cardsWithTypes["onePair"].append(card)
        else:
            cardsWithTypes["highCard"].append(card)

    return cardsWithTypes


def tieBreaker(cardsWithTypes: Dict[str, List[List[str]]]):
    def getRank(a: str):
        return 13 - cardRanks.index(a)
    
    def sorter(a: List[str], b: List[str]):
        for i in range(len(a[0])):
            if getRank(a[0][i]) == getRank(b[0][i]):
                continue
            return getRank(a[0][i]) - getRank(b[0][i])
        return 0
    
    rankedCards: List[List[str]] = []

    for _, card in cardsWithTypes.items():
        temp = sorted(card, key = cmp_to_key(sorter), reverse=True)

        rankedCards.extend(temp)

    return rankedCards


def calculateScore(cardsWithRanks: List[List[str]]):
    score = 0
    totalCars = len(cardsWithRanks)
    for idx, card in enumerate(cardsWithRanks):
        score = score + int(card[1]) * (totalCars - idx)
    return score

cardsMap: List[List[str]] = readInput()

modifiedCardMap = modifyJ(cardsMap=cardsMap)

cardsWithTypes: Dict[str, List[str]] = ruleParser(modifiedCardMap)

cardsWithRanks = tieBreaker(cardsWithTypes)

print(cardsWithRanks)

result = calculateScore(cardsWithRanks=cardsWithRanks)

print(result)
