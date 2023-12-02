from re import L

from matplotlib.cbook import maxdict


maxDict = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def main():
    with open("day2/input.txt","r") as file:
        content = file.readlines()
    gameSum = 0
    for game in content:
        gameValid = True
        game = game.strip().split(":")
        gameId = int(game[0].lstrip("Game"))
        game = game[1]
        for round in game.split(";"):
            for color in round.split(","):
                color = color.strip().split(" ")
                if int(color[0]) > maxDict[color[1]]:
                    gameValid = False
        if gameValid:
            gameSum += gameId
            
    print(gameSum)
if __name__ == '__main__':
    main()