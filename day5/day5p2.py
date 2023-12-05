from tqdm import tqdm

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
            rangeList.append({
                              "sourceStart":sourceStart,
                              "sourceRange":range(sourceStart,sourceStart+rangeLen),
                              "destinationStart":destinationStart,
                              "destinationRange":range(destinationStart,destinationStart+rangeLen),
                              "rangeLen":rangeLen
                              })
        mapDict[mapName] = rangeList
    
    return seeds,mapDict

def seedProcessor(seeds):
    seedRanges = []
    for i in range(0,len(seeds),2):
        seedRanges.append({"originalSeed":seeds[i],"seedRangeLen":seeds[i+1],"seedRange":range(seeds[i],seeds[i]+seeds[i+1])})
    return seedRanges
        


def main():
    with open("day5/input.txt","r") as file:
        content = file.read().strip()
    seeds,mapDict = getMappingDict(content)
    seedRanges = seedProcessor(seeds)
    lowestSeed = 0
    validSeedFound = False
    while not validSeedFound:
        seed = lowestSeed
        for mapName,mappingList in reversed(mapDict.items()):
            for growthMap in mappingList:
                destinationRange = growthMap["destinationRange"]
                if seed in destinationRange:
                    delta = seed - growthMap["destinationStart"]
                    seed = growthMap["sourceStart"] + delta
                    break
        
        for seedRange in seedRanges:
            if seed in seedRange["seedRange"]:
                print(f"Valid seed found {seed}")
                print(f"{lowestSeed=}")
                validSeedFound = True
                break
        else:
            lowestSeed+=1
            if lowestSeed % 1000000 == 0:
                print(lowestSeed)
        
        
        


if __name__ == '__main__':
    import time
    start_time = time.time()
    main()
    print('--- %s seconds ---' % (time.time() - start_time))