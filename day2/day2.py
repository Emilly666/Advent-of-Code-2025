from pathlib import Path

file = open(Path(__file__).with_name('input.txt'), "r" )
lines = file.read().split(',')

def part1(file):
  def isSequence(s):
    if len(s) % 2 == 1 : return False
    return s[int(len(s)/2):] == s[:int(len(s)/2)]
  
  sum = 0
  for r in file:
    (start, stop) = r.split('-')
    for num in range(int(start), int(stop) + 1):
      if isSequence(str(num)):
        sum += num

  return sum

def part2(file):
  def isSequence(s):
    return s in (s + s)[1:-1]
  
  sum = 0
  for r in file:
    (start, stop) = r.split('-')
    for num in range(int(start), int(stop) + 1):
      if isSequence(str(num)):
        sum += num

  return sum


#print(part1(lines))

print(part2(lines))