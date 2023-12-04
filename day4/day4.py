def main():
    with open("day4/input.txt","r") as file:
        content = file.read().replace("  "," ").split("\n")
    totalSum = 0
    for line in content:
        matches = -1
        line = line.split(":")[1]
        numbers = line.strip().split("|")
        winning = list(map(int,numbers[0].strip().split(" ")))
        gameNums = list(map(int,numbers[1].strip().split(" ")))
        for i in gameNums:
            if i in winning:
                matches +=1
        if matches >=0:
            totalSum += 2**matches
    print(totalSum)


if __name__ == '__main__':
    main()