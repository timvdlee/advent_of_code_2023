def convertDigitListToInt(inputList):
    return int("".join(map(str,inputList)))

def getMatrixDigitNeighbours(matrix,rowY,colX):
    neighbours = set([])
    try:
        neighbours.add(matrix[rowY-1][colX-1])
    except IndexError:
        pass
    try:
        neighbours.add(matrix[rowY-1][colX])
    except IndexError:
        pass
    try:
        neighbours.add(matrix[rowY-1][colX+1])
    except IndexError:
        pass
    
    
    try:
        neighbours.add(matrix[rowY][colX-1])
    except IndexError:
        pass
    try:
        neighbours.add(matrix[rowY][colX]) # Self
    except IndexError:
        pass
    try:
        neighbours.add(matrix[rowY][colX+1])
    except IndexError:
        pass
    
    try:
        neighbours.add(matrix[rowY+1][colX-1])
    except IndexError:
        pass
    try:
        neighbours.add(matrix[rowY+1][colX])
    except IndexError:
        pass
    try:
        neighbours.add(matrix[rowY+1][colX+1])
    except IndexError:
        pass
    return [x for x in neighbours if type(x) is int]

def getContentMatrix(content):
    parsedContentMatrix = []
        
    for line in content:
        parsedLine = []
        digitIndices = []
        digits = []
        previousDigit = False
        line = list(line)
        for i,char in enumerate(line):
            parsedLine.append(char)
            if char.isdigit():
                previousDigit = True
                digitIndices.append(i)
                digits.append(char)
            else:
                if previousDigit:
                    previousDigit=False
                    endDigit = convertDigitListToInt(digits)
                    for digitIndex in digitIndices:
                        parsedLine[digitIndex] = endDigit
                    digitIndices.clear()
                    digits.clear()
            
            if previousDigit and i+1 == len(line):
                previousDigit=False
                endDigit = convertDigitListToInt(digits)
                for digitIndex in digitIndices:
                    parsedLine[digitIndex] = endDigit
                digitIndices.clear()
                digits.clear()
        parsedContentMatrix.append(parsedLine)
    return parsedContentMatrix

def main():
    with open("day3/input.txt","r") as file:
        content = file.read().split("\n")
    
    matrix = getContentMatrix(content)
    totalSum = 0
    for rowY,row in enumerate(matrix):
        for colX,value in enumerate(row):
            if type(value) is not int and value != ".": #Symbol
                totalSum += sum(getMatrixDigitNeighbours(matrix,rowY,colX))
    print(totalSum)
    
    

if __name__ == '__main__':
    main()