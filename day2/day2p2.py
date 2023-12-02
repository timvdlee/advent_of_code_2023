
import math






def main():
    with open("day2/input.txt","r") as file:
        content = file.readlines()
    gameSum = 0
    for game in content:
        maxDict = {
        "red": 0,
        "green": 0,
        "blue": 0
        }   
        game = game.strip().split(":")
        game = game[1]
        for round in game.split(";"):
            for color in round.split(","):
                color = color.strip().split(" ")
                if int(color[0]) > int(maxDict[color[1]]):
                    maxDict[color[1]] = color[0]
        gameSum += math.prod(map(int,maxDict.values()))
                    
            
    print(gameSum)
    
    
if __name__ == '__main__':
    main()