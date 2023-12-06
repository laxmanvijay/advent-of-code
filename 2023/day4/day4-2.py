from typing import List


def readInput():
    with open("2023/day4/input.txt") as f:
        lines = f.readlines()

        games = {}

        for idx, line in enumerate(lines):
            totalCards = line.split(": ")[1]

            availableCards = totalCards.split("|")[1].strip().split()
            winningCards = totalCards.split("|")[0].strip().split()

            games[idx+1] = [availableCards, winningCards]
    
        return games

def calculateNewCardsForEachGame(winningCards: List[int], availableCards: List[int], gameId: int) -> int:
    availableWinningCards = set(availableCards).intersection(set(winningCards))

    score = len(availableWinningCards)
    newCards = []

    for i in range(gameId+1, score+1+gameId):
        newCards.append(i)

    return newCards


games = readInput()

new_cards = [] + list(games.keys())

i=0
while True:
    if i >= len(new_cards):
        break

    k = new_cards[i]
    i+=1
    v = games[k]

    new_cards += calculateNewCardsForEachGame(v[1], v[0], k)

print(len(new_cards))