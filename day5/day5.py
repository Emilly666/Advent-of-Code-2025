from pathlib import Path
from pprint import pprint

file = open(Path(__file__).with_name('input.txt'), "r" )
lines = file.read()

def part1(file: str):
  fresh_ingredients = 0
  ranges, ids = file.split('\n\n')
  ranges_list = []
  for range in ranges.split('\n'):
    range_from, range_to = range.split('-')
    ranges_list.append((int(range_from), int(range_to)))

  for id in ids.split('\n'):
    for range in ranges_list:
      if int(id) >= range[0] and int(id) <= range[1]: 
        fresh_ingredients += 1
        break

  return fresh_ingredients


def part2(file: str):
  ranges= file.split('\n\n')[0]
  ranges_list = []
  output_ranges = []
  for range_ in ranges.split('\n'):
    range_from, range_to = range_.split('-')
    ranges_list.append((int(range_from), int(range_to)))
  ranges_list = sorted(ranges_list, key = lambda x: x[0])

  current_range = ranges_list.pop(0)
  while len(ranges_list) > 0:
    next_range = ranges_list.pop(0)
    if next_range[0] <= current_range[1]:#combine
      current_range = (current_range[0], max([current_range[1], next_range[1]]))
    else:
      output_ranges.append(current_range)
      current_range = next_range
  else:
    output_ranges.append(current_range)

  return sum([x[1] - x[0] + 1 for x in output_ranges])



#print(part1(lines))

print(part2(lines))