
from numpy import tile
from tqdm import tqdm
import matplotlib

partsDict = {
    "|": [
        ["#"," ","#"],
        ["#"," ","#"],
        ["#"," ","#"]
    ],
    "-": [
        ["#","#","#"],
        [" "," "," "],
        ["#","#","#"],
    ], 
    "L": [
        ["#"," ","#"],
        ["#"," "," "],
        ["#","#","#"],   
    ],
    "J": [
        ["#"," ","#"],
        [" "," ","#"],
        ["#","#","#"],   
    ],
    "7": [
        ["#","#","#"],
        [" "," ","#"],
        ["#"," ","#"]
    ],
    "F": [
        ["#","#","#"],
        ["#"," "," "],
        ["#"," ","#"]
    ],
    ".": [
        ["#","#","#"],
        ["#","#","#"],
        ["#","#","#"],
    ],
    "S": [
        ["#"," ","#"],
        [" "," "," "],
        ["#"," ","#"],
    ]
}

def parseInput(content):
    blocksMatrix = []
    lines = content.splitlines()
    yLen = len(lines)
    for y,line in enumerate(lines):
        line = list(line)
        xLen = len(line)
        lineBlock = []
        for x,char in enumerate(line):
            lineBlock.append(partsDict[char])
            if char == "S":
                startPos = (x,y)
        blocksMatrix.append(lineBlock)
    return blocksMatrix,xLen,yLen,startPos
        
        
def convertGridTo2dMatrix(grid,xLen,yLen):
    endGrid = []
    for y in range(yLen*3):
        line = []
        for x in range(xLen*3):
            yLineIndex = y//3
            xblockIndex = x//3
            yblockLineIndex = y % 3
            xblockLineIndex = x % 3
            line.append(grid[yLineIndex][xblockIndex][yblockLineIndex][xblockLineIndex])
        endGrid.append(line)
    return endGrid

def contEval(matrixValue,currentValue):
    if matrixValue == " ":
        return True
    if matrixValue == "#":
        return False
    if currentValue > matrixValue:
        return False
    
def exploreMatrix(matrix2d,startPos):
    currentlyLookingAt = [startPos]
    matrix2d[startPos[1]][startPos[0]] = 0
    while currentlyLookingAt:
        x,y = currentlyLookingAt[0]
        currentValue = matrix2d[y][x]
        if contEval(matrix2d[y-1][x],currentValue):
            matrix2d[y-1][x] = currentValue + 1
            currentlyLookingAt.append((x,y-1))
        if contEval(matrix2d[y+1][x],currentValue):
            matrix2d[y+1][x] = currentValue + 1
            currentlyLookingAt.append((x,y+1))
        if contEval(matrix2d[y][x-1],currentValue):
            matrix2d[y][x-1] = currentValue + 1
            currentlyLookingAt.append((x-1,y))
        if contEval(matrix2d[y][x+1],currentValue):
            matrix2d[y][x+1] = currentValue + 1
            currentlyLookingAt.append((x+1,y))
        del currentlyLookingAt[0]
    
    endPos = (None,None)
    maxVal = 0
    for y,line in enumerate(matrix2d):
        for x,char in enumerate(line):
            if isinstance(char,int):
                if char > maxVal:
                    maxVal = char
                    endPos = (x,y)
                    
    return matrix2d,startPos,endPos


def traceEval(matrixValue,currentValue,pos,previousPath):
    if pos in previousPath:
        return False
    if matrixValue == "#":
        return False
    if currentValue > matrixValue:
        return True
    return False

def findPath(matrix2d,endPos,previousPath=[]):
    path = []
    currentlyLookingAt = [endPos]
    while currentlyLookingAt:
        x,y = currentlyLookingAt[0]
        currentValue = matrix2d[y][x]
        if traceEval(matrix2d[y-1][x],currentValue,(x,y-1),previousPath):
            currentlyLookingAt.append((x,y-1))
            path.append((x,y-1))
        elif traceEval(matrix2d[y+1][x],currentValue,(x,y+1),previousPath):
            currentlyLookingAt.append((x,y+1))
            path.append((x,y+1))
        elif traceEval(matrix2d[y][x-1],currentValue,(x-1,y),previousPath):
            currentlyLookingAt.append((x-1,y))
            path.append((x-1,y))
        elif traceEval(matrix2d[y][x+1],currentValue,(x+1,y),previousPath):
            currentlyLookingAt.append((x+1,y))
            path.append((x+1,y))
        del currentlyLookingAt[0]
    
    return path
    
def innerPathFinder(matrix2d,loop):
    nonLoop = getNonLoop(matrix2d,loop)
    loop = matplotlib.path.Path(loop)
    withinLoop = set([])
    for nonLoopCoord in tqdm(nonLoop,desc="Checking if point in loop"):
        if loop.contains_point(nonLoopCoord): # This tip i took from someone else but it was useful!
            withinLoop.add(nonLoopCoord)
    return withinLoop
    

def getNonLoop(matrix2d,loop):
    nonLoopTiles = []
    for y,v in enumerate(tqdm(matrix2d,desc="Getting Non loop values")):
        for x,_ in enumerate(v):
            if (x,y) not in loop:
                nonLoopTiles.append((x,y))
    return nonLoopTiles
import math

def main():
    with open("day10/example.txt","r") as file:
        strGrid,xLen,yLen,startPos = parseInput(file.read().strip())
    matrix2d = convertGridTo2dMatrix(strGrid,xLen,yLen)
    startIndices = ((startPos[0]*3)+1,(startPos[1]*3)+1)
    print("expl")
    matrix2d,startPos,endPos = exploreMatrix(matrix2d,startIndices)
    print("findingPath")
    path1 = findPath(matrix2d,endPos)
    print("doneWith1")
    path2 = findPath(matrix2d,endPos,previousPath=path1)
    path1.insert(0,endPos)
    path2.append(startPos)
    combinedLoop = list(reversed(path1)) + path2
    print("FindInner")
    tilesIncluded = innerPathFinder(matrix2d,combinedLoop)
    for x,y in tilesIncluded:
        matrix2d[y][x] = "@"
    print(f"{len(tilesIncluded)=}")
    print(print(f"{len(combinedLoop)=}"))
    trueInval = len(tilesIncluded)-len(combinedLoop)
    print(trueInval//9 + 1)
    
    
if __name__ == '__main__':
    import time
    start_time = time.time()
    main()
    print('--- %s seconds ---' % (time.time() - start_time))
    
# if __name__ == '__main__':
#     from datetime import datetime
#     start_time = datetime.now()
#     # print(f"Started at: {start_time.strftime('%H:%M:%S')}")
#     main()
#     print('--- %s seconds ---' % (datetime.now() - start_time))