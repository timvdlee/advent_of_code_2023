from itertools import product
from tqdm import tqdm

def parseInput(content):
    contentList = []
    for c in content.splitlines():
        springList = []
        springMap,brokenCount = c.split(" ")
        springList.append(list(springMap))
        springList.append(list(map(int,brokenCount.split(","))))
        contentList.append(springList)
    return contentList

def consecutiveBrokenMapper(springList):
    convertedSlist = []
    previousCLen = 0
    for c in springList:
        if c == "#":
            previousCLen += 1
        else:
            if previousCLen > 0:
                convertedSlist.append(previousCLen)
            previousCLen = 0
    if previousCLen > 0:
        convertedSlist.append(previousCLen)
    return convertedSlist

def lineValidator(springlist,brokenMap):
    # if "?" in springlist:
    #     return False
    if sum(brokenMap) != springlist.count("#"):
        return False
    return brokenMap == consecutiveBrokenMapper(springlist)
    


    

def combinationCreator(springList,brokenMap):
    wildCardLocation = []
    for i,c in enumerate(springList):
        if c == "?":
            wildCardLocation.append(i)
    questionCount = len(wildCardLocation)
    possibleCombinations = product([".","#"],repeat=questionCount)
    possibleValidCom = 0
    for combi in possibleCombinations:
        for qIndex,combiOpt in zip(wildCardLocation,combi):
            springList[qIndex] = combiOpt
        if lineValidator(springList,brokenMap):
            possibleValidCom+=1
    return possibleValidCom
            
        
        
        
def findCombinations(contentLine):
    springList,brokenMap = contentLine
    return combinationCreator(list(springList),brokenMap)
    
        

def main():
    with open("day12/input.txt","r") as file:
        inputs = parseInput(file.read().strip())
    s = 0
    for line in tqdm(inputs):
        s+= findCombinations(line)
    print(s)
"""        
???.### 1,1,3 - 1 arrangement
.??..??...?##. 1,1,3 - 4 arrangements
?#?#?#?#?#?#?#? 1,3,1,6 - 1 arrangement
????.#...#... 4,1,1 - 1 arrangement
????.######..#####. 1,6,5 - 4 arrangements
?###???????? 3,2,1 - 10 arrangements
"""


if __name__ == '__main__':
    import time
    start_time = time.time()
    main()
    print('--- %s seconds ---' % (time.time() - start_time))