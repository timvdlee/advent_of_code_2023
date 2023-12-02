import re

def findAndReplaceFirst(inputString:str,matches:dict):
    minIndex = 1000
    minMatch = None
    for match in matches:
        i = inputString.find(match)
        if i == -1:
            i = 1000
        if i < minIndex:
            minIndex = i
            minMatch = match
    if minMatch:
        return inputString.replace(minMatch,matches[minMatch],1)
    else:
        return inputString

mapDict = {"one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
revMapDict = {k[::-1]:v for k,v in mapDict.items()}


def part2LineParser(line:str):
    line = findAndReplaceFirst(line,mapDict)
    line = findAndReplaceFirst(line[::-1],revMapDict)[::-1]
    return line
    




def main():
    telsum = 0
    with open("day1/input.txt") as file:
        content = file.readlines()
        for line in content:
            line = line.strip()
            line = part2LineParser(line)
            for charFor in line:
                if charFor.isdigit():
                    break
            for charRev in reversed(line):
                if charRev.isdigit():
                    break
            telsum += int(charFor+charRev)
        
    print(telsum)


if __name__ == '__main__':
    main()
    # print(part2LineParser("sixdddkcqjdnzzrgfourxjtwosevenhg9"))