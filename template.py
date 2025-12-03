from pathlib import Path

file = open(Path(__file__).with_name('test.txt'), "r" )
lines = file.read().split('\n')

def part1(file):
  return file


def part2(file):
  return file



print(part1(lines))

#print(part2(lines))