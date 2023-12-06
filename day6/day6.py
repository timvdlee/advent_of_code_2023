import math

def parseInput(content):
    content = content.replace("    "," ").replace("   "," ").replace("  "," ")
    times,distances = content.split("\n")
    times = list(map(int,times.split(":")[1].strip().split(" ")))
    distances = list(map(int,distances.split(":")[1].strip().split(" ")))
    endList = []
    for time,distance in zip(times,distances):
        endList.append({"time":time,"distance":distance})
    return endList

def main():
    with open("day6/input.txt") as file:
        content = file.read().strip()
    distanceTimeList = parseInput(content)
    waysOfWinning = []
    for distanceTime in distanceTimeList:
        winCount = 0
        maxTime = distanceTime["time"]
        for i in range(maxTime):
            speed = i
            timeLeft = maxTime - i
            distanceTraveled = speed * timeLeft
            if distanceTraveled > distanceTime["distance"]:
                winCount += 1
        waysOfWinning.append(winCount)
    print(math.prod(waysOfWinning))

if __name__ == '__main__':
    main()