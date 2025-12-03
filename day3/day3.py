from pathlib import Path
from typing import List

file = open(Path(__file__).with_name('input.txt'), "r" )
lines = file.read().split('\n')

def part1(file: List[str]):
  joltage = 0
  for line in file:
    max1 = max(list(line))
    i1 = line.index(max1)
    line2 = line.replace(max1, '0', 1)
    if i1 == len(line) - 1:
      max2 = max(list(line2))
      joltage += int(max2 + max1)
    else:
      max2 = max(list(line2[i1:]))
      joltage += int(max1 + max2)

  return joltage


def part2(file: List[str]):
  batteries = 12
  joltage = 0
  for line in file:
    line = [int(x) for x in line]
    jolts = ''
    max_i = 0
    for i in range(1, batteries + 1):
      end_i = -(batteries - i) if (batteries - i) > 0 else len(line)
      max_b = max(line[max_i : end_i])
      max_i = line[max_i : end_i].index(max_b) + max_i + 1
      jolts += str(max_b)
    joltage += int(jolts)

  return joltage


#print(part1(lines))

print(part2(lines))