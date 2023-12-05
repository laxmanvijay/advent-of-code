from typing import List


def readInput():
    with open("2023/day4/input.txt") as f:
        lines = f.readlines()

        games = []

        for line in lines:
            totalCards = line.split(": ")[1]

            availableCards = totalCards.split("|")[1].strip().split()
            winningCards = totalCards.split("|")[0].strip().split()

            games.append([availableCards, winningCards])
    
        return games

def calculateScoreForEachGame(winningCards: List[int], availableCards: List[int]) -> int:
    score = 0
    availableWinningCards = set(availableCards).intersection(set(winningCards))

    if len(availableWinningCards) > 0:
        score = 1

    score = score * 2**(len(availableWinningCards) - 1)

    return score

def calculateTotalScore(games: List) -> bool:
    totalScore = 0
    for g in games:
        totalScore += calculateScoreForEachGame(g[0], g[1])
    
    return totalScore

games = readInput()
print(calculateTotalScore(games))