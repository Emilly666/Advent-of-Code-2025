from pathlib import Path
from pprint import pprint
from typing import List
import math
import itertools

file = open(Path(__file__).with_name('input.txt'), "r" )
lines = file.read().split('\n')

def part1(file: List[str]):
  connections = 10 if len(file) < 1000 else 1000
  boxes = [ list(map(int,row.split(','))) for row in file]
  distances = []
  for pair in list(itertools.combinations(enumerate(boxes), 2)):
    distances.append([pair[0][0], pair[1][0], distance(pair[0][1], pair[1][1])])
  distances.sort(key=lambda x: x[2])
  
  distances = [distance[:2] for distance in distances[:connections]]
  circuits = []

  for dist in distances:
    index1 = next((i for i, lst in enumerate(circuits) if dist[0] in lst), None)
    index2 = next((i for i, lst in enumerate(circuits) if dist[1] in lst), None)

    if index1 is None and index2 is None: 
      circuits.append([dist[0], dist[1]])
    elif index1 is None and index2 is not None: 
      circuits[index2].append(dist[0])
    elif index1 is not None and index2 is None: 
      circuits[index1].append(dist[1])
    elif index1 != index2:
      c1 = circuits[index1]
      c2 = circuits[index2]
      circuits.remove(c1)
      circuits.remove(c2)
      circuits.append(c1+c2)

  circuits.sort(key=lambda item: len(item), reverse=True)

  return math.prod(len(c) for c in circuits[:3])


def part2(file: List[str]):
  boxes = [ list(map(int,row.split(','))) for row in file]
  distances = []
  for pair in list(itertools.combinations(enumerate(boxes), 2)):
    distances.append([pair[0][0], pair[1][0], distance(pair[0][1], pair[1][1])])
  distances.sort(key=lambda x: x[2])
  
  distances = [distance[:2] for distance in distances]
  circuits = [[i] for i in range(len(boxes))]

  while len(circuits) > 1:
    dist = distances.pop(0)
    index1 = next((i for i, lst in enumerate(circuits) if dist[0] in lst), None)
    index2 = next((i for i, lst in enumerate(circuits) if dist[1] in lst), None)
    if index1 == index2: continue
    c1 = circuits[index1]
    c2 = circuits[index2]
    circuits.remove(c1)
    circuits.remove(c2)
    circuits.append(c1 + c2)

  return boxes[dist[0]][0] * boxes[dist[1]][0]

def distance(a: tuple[int, int, int], b: tuple[int, int, int]):
  x1, y1, z1 = a
  x2, y2, z2 = b
  return math.sqrt( (x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2 )

#pprint(part1(lines))

pprint(part2(lines))