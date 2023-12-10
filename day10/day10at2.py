
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from tqdm import tqdm
from multiprocessing import Pool
from collections import deque


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
    # for l in grid:
    #     print(l)
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
    
def findPath(matrix2d,startPos):
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
        
    maxVal = 0
    for line in matrix2d:
        for char in line:
            if isinstance(char,int):
                if char > maxVal:
                    maxVal = char
                    
    print(maxVal)
    print(maxVal//3)
    


def main():
    with open("day10/input.txt","r") as file:
        strGrid,xLen,yLen,startPos = parseInput(file.read().strip())
    matrix2d = convertGridTo2dMatrix(strGrid,xLen,yLen)
    startIndices = ((startPos[0]*3)+1,(startPos[1]*3)+1)
    endPost = findPath(matrix2d,startIndices)
    
    
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