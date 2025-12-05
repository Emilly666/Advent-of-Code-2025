from pathlib import Path
from typing import List

file = open(Path(__file__).with_name('test.txt'), "r" )
lines = file.read().split('\n')

def part1(file: List[str]):
  return file


def part2(file: List[str]):
  return file



print(part1(lines))

#print(part2(lines))