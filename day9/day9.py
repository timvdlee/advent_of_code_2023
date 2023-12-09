
def parseInput(content):
    return [list(map(int,line.split())) for line in content.splitlines()]
    
    
def buildNumberTree(numberList):
    # We technically only need the last value once the tree has been build
    numberTree = [numberList]
    while numberTree[-1] != [0]*len(numberTree[-1]):
        nextNumReeks = []
        lastNums = numberTree[-1]
        for i in range(0,len(lastNums)-1):
            nextNumReeks.append(lastNums[i+1]-lastNums[i])
        numberTree.append(nextNumReeks)
    return numberTree
    
def predictNextNum(numberTree):
    addToNextCycle = 0
    for nums in reversed(numberTree):
        nums.append(nums[-1]+addToNextCycle)
        addToNextCycle = nums[-1]
    return numberTree[0][-1]



def main():
    with open("day9/example.txt") as file:
        numbers = parseInput(file.read().strip())

    nextNumList = []
    for nextNums  in numbers:
        numberTree = buildNumberTree(nextNums)
        print(numberTree)
        nextNumList.append(predictNextNum(numberTree))
    print(nextNumList)
    print(sum(nextNumList))
     
        
if __name__ == '__main__':
    import time
    start_time = time.time()
    main()
    print('--- %s seconds ---' % (time.time() - start_time))