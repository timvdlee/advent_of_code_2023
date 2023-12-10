
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from tqdm import tqdm
from multiprocessing import Pool


partsDict = {
    "|": [
        [0,1,0],
        [0,1,0],
        [0,1,0]
    ],
    "-": [
        [0,0,0],
        [1,1,1],
        [0,0,0],
    ], 
    "L": [
        [0,1,0],
        [0,1,1],
        [0,0,0],   
    ],
    "J": [
        [0,1,0],
        [1,1,0],
        [0,0,0],   
    ],
    "7": [
        [0,0,0],
        [1,1,0],
        [0,1,0]
    ],
    "F": [
        [0,0,0],
        [0,1,1],
        [0,1,0]
    ],
    ".": [
        [0,0,0],
        [0,0,0],
        [0,0,0],
    ],
    "S": [
        [0,1,0],
        [1,1,1],
        [0,1,0],
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
                startPos = (y,x)
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
globalPathList = []
    
def findPath(matrix2d,startPos,end):
    grid = Grid(matrix=matrix2d)
    start = grid.node(*startPos)
    end = grid.node(*end)
    finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
    path,runs = finder.find_path(start,end,grid)
    globalPathList.append(path)
    return len(path) -1


def main():
    with open("day10/input.txt","r") as file:
        strGrid,xLen,yLen,startPos = parseInput(file.read().strip())
    matrix2d = convertGridTo2dMatrix(strGrid,xLen,yLen)
    startIndices = ((startPos[0]*3)+1,(startPos[1]*3)+1)
    innitArgs = []
    c = 0
    for y in tqdm(range(yLen)):
        for x in range(xLen):
            endIndices = ((x*3)+1,(y*3)+1)
            if matrix2d[endIndices[1]][endIndices[0]] == 0:
                continue
            c+=1
            innitArgs.append([matrix2d,startIndices,endIndices])
    print(c)
    print(len(innitArgs[0]))
    with Pool(16) as p:
        pathLenList = p.starmap(findPath,innitArgs[0])
            
    print(max(pathLenList))
    print("awns")
    print(max(pathLenList)//3)
    
    
    
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