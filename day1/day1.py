from pathlib import Path

file = open(Path(__file__).with_name('input.txt'), "r" )
lines = file.read().split('\n')

### Solutions ##############################

def part1(file: list):
  val = 50
  count = 0

  for command in file:
    (dir, steps) = (command[:1], command[1:])
    if dir == 'L':
      val = (val - int(steps)) % 100
    else:
      val = (val + int(steps)) % 100
    if val == 0 : count += 1

  return count


def part2(file):
  val = 50
  count = 0

  for command in file:
    (dir, steps) = (command[:1], int(command[1:]))
    for _ in range(steps):
      val = val - 1 if dir == 'L' else val + 1
      if val == 0: 
        count += 1
      elif val == 100: 
        count += 1
      val = val % 100

  return count

### Function calls: ##############################

#print(part1(lines))

print(part2(lines))