import re
# This took me like 5 hours to figure out. 
# It ended up being too hight by 1 and I have no clue why
map = {
	"one": 1,
	"two": 2,
	"three": 3,
	"four": 4,
	"five": 5,
	"six": 6,
	"seven": 7,
	"eight": 8,
	"nine": 9
}


def conv(s):
    if s in map:
        return str(map[s])
    else:
        return s


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