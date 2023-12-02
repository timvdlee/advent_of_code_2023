import re

r = '1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine'

def f(line):
  x = [*map({n: i%9+1 for i, n in enumerate(r.split('|'))}.get,
    re.findall(rf'(?=({r}))', line))]
  return 10*x[0] + x[-1]

print(sum(map(f, open('day1/input.txt'))))
