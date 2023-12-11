import numpy as np
import pandas as pd
from tqdm import tqdm

EXPANSIONRATE = 1000000

def parseInput(content):
    gNum = 1
    spaceMatrix = []
    for line in content.splitlines():
        spaceBand = []
        for char in line:
            if char == "#":
                spaceBand.append(gNum)
                gNum += 1
            else:
                spaceBand.append(char)
        spaceMatrix.append(spaceBand)
    return pd.DataFrame(spaceMatrix)

def getExpansionLocation(spaceMatrix):
    colsToExpand = []
    rowsToExpand = []
    for i in range(len(spaceMatrix)): #rows
        if len(set(spaceMatrix.iloc[i,:])) == 1:
            rowsToExpand.append(i)
    for i in range(len(spaceMatrix[0])): #cols
        if len(set(spaceMatrix.iloc[:,i])) == 1:
            colsToExpand.append(i)
    return colsToExpand,rowsToExpand

def expandUniverse(spaceMatrix,colsToExpand,rowsToExpand):
    colLen = len(spaceMatrix)
    rowLen = len(spaceMatrix[0])
    for x in tqdm(sorted(colsToExpand,reverse=True)):
        for _ in range(EXPANSIONRATE-1):
            colToAdd = pd.DataFrame(["."]*colLen)
            spaceMatrix.insert(x,x,colToAdd,allow_duplicates=True)
        
    for y in sorted(rowsToExpand,reverse=True):
        for _ in range(EXPANSIONRATE-1):
            rowToAdd = pd.DataFrame(["."]*rowLen).transpose()
            spaceMatrix = pd.concat([spaceMatrix.iloc[:y], rowToAdd, spaceMatrix.iloc[y:]]).reset_index(drop=True)
        
    return spaceMatrix

def getGalaxyIndices(expandedUniverse):
    spaceMatrix = expandedUniverse.to_numpy()
    galaxies = {}
    for y,yVals in enumerate(spaceMatrix):
        for x,val in enumerate(yVals):
            if val != ".":
                galaxies[val] = (x,y)
    return galaxies



def expandGalaxiesIndices(galaxies,rowsToExpand,colsToExpand):
    newGalaxyDict = {}
    for k,v in galaxies.items():
        x,y = v
        newX = x
        newY = y
        for row in rowsToExpand:
            if y > row:
                newY += EXPANSIONRATE-1
        for col in colsToExpand:
            if x > col:
                newX += EXPANSIONRATE-1
        newGalaxyDict[k] = (newX,newY)
    return newGalaxyDict
        
        

def main():
    with open("day11/input.txt","r") as file:
        spaceMatrix = parseInput(file.read().strip())
    colsToExpand,rowsToExpand = getExpansionLocation(spaceMatrix)
    galaxies = getGalaxyIndices(spaceMatrix)
    # expandedUniverse = expandUniverse(spaceMatrix,colsToExpand,rowsToExpand)
    galaxies = expandGalaxiesIndices(galaxies,rowsToExpand,colsToExpand)
    distanceDict = {}
    for k1,v1 in galaxies.items():
        for k2,v2 in galaxies.items():
            if k1 != k2:
                compositeKey = "|".join(map(str,sorted([k1,k2])))
                if compositeKey not in distanceDict:
                    distanceDict[compositeKey] = abs(v1[0]-v2[0]) + abs(v1[1]-v2[1])
    print(sum(distanceDict.values()))
                
        

    
if __name__ == '__main__':
    import time
    start_time = time.time()
    main()
    print('--- %s seconds ---' % (time.time() - start_time))