def getMappingDict(content):
    mapDict = {}
    splittedSections = content.split("\n\n")
    seeds = list(map(int,splittedSections[0].split(":")[1].strip().split(" ")))
    maps = splittedSections[1:]
    for alMap in maps:
        alMap = alMap.split(":")
        mapName = alMap[0]
        rangeList = []
        for mapping in alMap[1].strip().split("\n"):
            destinationStart,sourceStart,rangeLen = tuple(map(int,mapping.split(" ")))
            rangeList.append({"destinationStart":destinationStart,"range":range(sourceStart,sourceStart+rangeLen),"sourceStart":sourceStart,"rangeLen":rangeLen})
        mapDict[mapName] = rangeList
    
    return seeds,mapDict

def main():
    with open("day5/input.txt","r") as file:
        content = file.read().strip()
    seeds,mapDict = getMappingDict(content)
    locList = []
    for seed in seeds:
        for mapName,mapping in mapDict.items():
            # print(mapName,mapping)
            for growthMap in mapping:
                growthRange = growthMap["range"]
                if seed in growthMap["range"]:
                    delta = seed - growthMap["sourceStart"]
                    seed = growthMap["destinationStart"] + delta
                    break
        locList.append(seed)
    print(locList)
    print(min(locList))

if __name__ == '__main__':
    main()