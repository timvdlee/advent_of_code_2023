
def parseInput(content):
    lookupDict = {}
    content = content.split("\n\n")
    instructions = list(content[0].strip())
    for lookup in content[1].split("\n"):
        key,valueString = lookup.replace(" ","").split("=")
        values = tuple(valueString.strip("()").split(",")) # Maybe convert to indexes instead
        lookupDict[key] = values
    return instructions,lookupDict


def convertRLToIndex(RL):
    return 0 if RL == "L" else 1

def convertInstructionsToIndices(instructions):
    return list(map(convertRLToIndex,instructions))


def convertLookupTableToList(lookupTable):
    endList = []
    dictAsList = list(lookupTable)
    startIndex = None
    endResultIndex = None
    for k,v in lookupTable.items():
        indexLeft = dictAsList.index(v[0])
        indexRight = dictAsList.index(v[1])
        endList.append((indexLeft,indexRight))
        if k == "ZZZ":
            endResultIndex = dictAsList.index("ZZZ")
        if k == "AAA":
            startIndex = dictAsList.index("AAA")

    return endList,startIndex,endResultIndex

def main():
    with open("day8/input.txt","r") as file:
        instructions, lookupTable  = parseInput(file.read().strip())
    
    instructions = convertInstructionsToIndices(instructions)
    lookupTable,aaaIndex,zzzIndex = convertLookupTableToList(lookupTable)  
    print(f"{zzzIndex=}")
    
    steps = 0
    instructionIndex= 0
    location = aaaIndex
    while True:
        location = lookupTable[location][instructions[instructionIndex]]
        steps +=1
        instructionIndex += 1
        if instructionIndex == len(instructions):
            instructionIndex = 0
        if location == zzzIndex:
            break
        
    print(steps)




if __name__ == '__main__':
    import time
    start_time = time.time()
    main()
    print('--- %s seconds ---' % (time.time() - start_time))