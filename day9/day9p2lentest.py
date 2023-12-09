from tqdm import tqdm

def parseInput(content):
    return [list(map(int,line.split())) for line in content.splitlines()]
    
    
def buildNumberTree(numberList):
    numberTree = [numberList]
    while numberTree[-1] != [0]*len(numberTree[-1]):
        nextNumReeks = []
        lastNums = numberTree[-1]
        for i in range(0,len(lastNums)-1):
            nextNumReeks.append(lastNums[i]-lastNums[i+1])
        numberTree.append(nextNumReeks)
    return numberTree
    
def predictNextNum(numberTree):
    addToNextCycle = 0
    for nums in reversed(numberTree):
        nums.insert(0,(nums[0]+addToNextCycle))
        addToNextCycle = nums[0]
    return numberTree[0][0]



def main():
    with open("day9/input.txt") as file:
        numbers = parseInput(file.read().strip())

    nextNumList = []
    for nextNums  in numbers:
        numberTree = buildNumberTree(nextNums)
        nextNumList.append(predictNextNum(numberTree))

    print(sum(nextNumList))
     
        
if __name__ == '__main__':
    import time
    start_time = time.time()
    main()
    print('--- %s seconds ---' % (time.time() - start_time))