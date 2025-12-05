from pathlib import Path
from typing import List

file = open(Path(__file__).with_name('input.txt'), "r" )
lines = file.read().split('\n')

def part1(file: List[str]):
  grid = [list(line) for line in file]
  accesible_rolls = 0

  for x in range(len(grid)):
    for y in range(len(grid[x])):
      if grid[x][y] != '@':
        continue
      rolls_around = 0
      if x > 0 and grid[x-1][y] in ('@', 'x'): rolls_around += 1
      if x < len(grid[x]) - 1 and grid[x+1][y] in ('@', 'x'): rolls_around += 1
      if y > 0 and grid[x][y-1] in ('@', 'x'): rolls_around += 1
      if y < len(grid) - 1 and grid[x][y+1] in ('@', 'x'): rolls_around += 1
      if x > 0 and y > 0 and grid[x-1][y-1] in ('@', 'x'): rolls_around += 1
      if x < len(grid[x]) - 1 and y > 0 and grid[x+1][y-1] in ('@', 'x'): rolls_around += 1
      if x > 0 and y < len(grid) - 1 and grid[x-1][y+1] in ('@', 'x'): rolls_around += 1
      if x < len(grid[x]) - 1 and y < len(grid) - 1 and grid[x+1][y+1] in ('@', 'x'): rolls_around += 1
      
      if rolls_around < 4:
        accesible_rolls += 1
        grid[x][y] = 'x'
  return accesible_rolls


def part2(file: List[str]):
  grid = [list(line) for line in file]
  removed_rolls = 0
  can_remove = True
  while can_remove:
    accesible_rolls = 0
    for x in range(len(grid)):
      for y in range(len(grid[x])):
        if grid[x][y] != '@':
          continue
        rolls_around = 0
        if x > 0 and grid[x-1][y] != '.': rolls_around += 1
        if x < len(grid[x]) - 1 and grid[x+1][y] != '.': rolls_around += 1
        if y > 0 and grid[x][y-1] != '.': rolls_around += 1
        if y < len(grid) - 1 and grid[x][y+1] != '.': rolls_around += 1
        if x > 0 and y > 0 and grid[x-1][y-1] != '.': rolls_around += 1
        if x < len(grid[x]) - 1 and y > 0 and grid[x+1][y-1] != '.': rolls_around += 1
        if x > 0 and y < len(grid) - 1 and grid[x-1][y+1] != '.': rolls_around += 1
        if x < len(grid[x]) - 1 and y < len(grid) - 1 and grid[x+1][y+1] != '.': rolls_around += 1
        
        if rolls_around < 4:
          accesible_rolls += 1
          grid[x][y] = 'x'
        
    if accesible_rolls == 0:
      can_remove = False
    else: 
      removed_rolls += accesible_rolls

    for x in range(len(grid)):
      for y in range(len(grid[x])):
        if grid[x][y] == 'x': grid[x][y] = '.'

  return removed_rolls



#print(part1(lines))

print(part2(lines))