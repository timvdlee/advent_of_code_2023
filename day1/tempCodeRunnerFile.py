
def main():
    with open("day1/input.txt","r") as file:
        content = file.readlines()
    numSum = 0
    pattern = "|".join([k for k in map]+[str(v) for v in map.values()])
    print(pattern)
    for line in content:
        line = line.strip()
        matches = re.findall(pattern,line)
        numSum += int(conv(matches[0]) + conv(matches[-1]))
        
    
    print(numSum)
if __name__ == '__main__':
    main()