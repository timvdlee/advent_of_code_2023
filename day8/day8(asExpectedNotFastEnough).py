
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

def main():
    with open("day8/example.txt","r") as file:
        instructions, lookupTable  = parseInput(file.read().strip())
    
    steps = 0
    instructionIndex= 0
    location = next(iter(lookupTable))
    while True:
        possibleJumps = lookupTable[location]
        currentInstruction = instructions[instructionIndex]
        location = possibleJumps[convertRLToIndex(currentInstruction)]
        steps +=1
        instructionIndex += 1
        if instructionIndex == len(instructions):
            instructionIndex = 0
        
        if location == "ZZZ":
            break
    print(steps)




if __name__ == '__main__':
    import time
    start_time = time.time()
    main()
    print('--- %s seconds ---' % (time.time() - start_time))