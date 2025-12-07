from pathlib import Path
from pprint import pprint
from typing import List
from functools import cache

file = open(Path(__file__).with_name('input.txt'), "r" )
lines = file.read().split('\n')

def part1(file: List[str]):
  splittings = 0
  q = set()
  q.add((1,file[0].index('S')))
  while len(q) > 0:
    x, y = q.pop()
    if x == len(file) - 1:
      continue
    if file[x + 1][y] == '^':
      q.add((x + 1, y - 1))
      file[x + 1] = file[x + 1][:y - 1] + '|' + file[x + 1][y:]
      q.add((x + 1, y + 1))
      file[x + 1] = file[x + 1][:y + 1] + '|' + file[x + 1][y + 2:]
      splittings += 1
    elif  file[x + 1][y] == '.':
      q.add((x + 1, y))
      file[x + 1] = file[x + 1][:y] + '|' + file[x + 1][y + 1:]

  return splittings


def part2(file: List[str]):
  @cache
  def solve(row, col):
    if row == len(file) - 1:
      return 1

    if file[row][col] == '.':
      return solve(row + 1, col)
    elif file[row][col] == '^':
      return solve(row + 1, col - 1) + solve(row + 1, col + 1)

  return solve(1, file[0].index('S'))



#pprint(part1(lines))

pprint(part2(lines))