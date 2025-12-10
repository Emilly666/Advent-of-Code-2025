from pathlib import Path
from pprint import pprint
from typing import List
import math
import itertools

file = open(Path(__file__).with_name('test.txt'), "r" )
lines = file.read().split('\n')

def part1(file: List[str]):
  red_tiles = [ list(map(int,row.split(','))) for row in file]
  distances = []
  for a, b in list(itertools.combinations(red_tiles, 2)):
    distances.append((abs(a[1] - b[1]) + 1) * (abs(a[0] - b[0]) + 1))

  distances.sort(reverse=True)

  return distances[0]


def part2(file: List[str]):

  return 

#pprint(part1(lines))

pprint(part2(lines))