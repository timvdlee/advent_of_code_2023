def main():
    with open("day4/input.txt","r") as file:
        content = file.read().replace("  "," ").split("\n")
    scratchCardNum = [1 for _ in content]
    winTracker = []
    for i,line in enumerate(content):
        matches = 0
        originalLine = line
        line = line.split(":")
        index = line[0].lstrip("Card ")
        numbers = line[1].strip().split("|")
        winning = list(map(int,numbers[0].strip().split(" ")))
        gameNums = list(map(int,numbers[1].strip().split(" ")))
        for num in gameNums:
            if num in winning:
                matches +=1
        winTracker.append(matches)

    for i,zp in enumerate(zip(winTracker,scratchCardNum)):
        wins, numOfCards = zp
        for j in range(wins):
            scratchCardNum[i+1+j] += numOfCards
    print(sum(scratchCardNum))

if __name__ == '__main__':
    main()