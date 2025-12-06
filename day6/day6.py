from pathlib import Path
import re
from pprint import pprint
from typing import List

file = open(Path(__file__).with_name('input.txt'), "r" )
lines = file.read().split('\n')

def part1(file: List[str]):
  result = 0
  numbers_arrays = []
  operations = []
  for index, line in enumerate(file):
    if index < len(file) - 1:
      numbers_arrays.append(list(map(int, re.sub(' +', ' ', line).strip().split(' '))))
    else:
      operations = re.sub(' +', ' ', line).strip().split(' ')
  
  for index, operation in enumerate(operations):
    output = 0
    if operation == '+':
      for numbers in numbers_arrays:
        output += numbers[index]
    elif operation == '*':
      if output == 0 : output = 1
      for numbers in numbers_arrays:
        output *= numbers[index]
    result += output

  return result


def part2(file: List[str]):
  result = 0
  index = len(file[0]) -1
  numbers = []
  while index >= 0:
    number = ''
    for i, line in enumerate(file):
      if i == len(file) - 1:
        numbers.append(int(number))
        number = ''
      if line[index] == ' ':
        continue
      elif line[index] in '0123456789':
        number += line[index]
      elif line[index] in '+*':
        print(numbers)
        output = numbers.pop()
        for number in numbers:
          if line[index] == '+': output += number
          elif line[index] == '*': output *= number
        result += output
        numbers = []
        index -= 1
    index -= 1

  return result


#pprint(part1(lines))

pprint(part2(lines))