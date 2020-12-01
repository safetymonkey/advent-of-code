""" ???
Part 1: ???
Part 2: ???
https://adventofcode.com/2018/day/3
"""

import re

def parse_input(filename):
  """Convenience method to parse a file and return a list as input"""
  fabrics = []
  with open(filename, 'r') as input_file:
    for line in input_file:
      match = re.match(r'\#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', line)
      fabrics.append({'id': int(match[1]), 'left_margin': int(match[2]),
                      'top_margin': int(match[3]), 'width': int(match[4]),
                      'height': int(match[5])})
  return fabrics


def generate_overlap(input_list):
  """ Take the input list and generate a list of coordinates that have overlap """
  seen_coordinates = set()
  overlapping_coordinates = set()
  for claim in input_list:
    for x in range(1, claim['width']+ 1):
      for y in range(1, claim['height'] + 1):
        coordinates = (claim['left_margin'] + x, claim['top_margin'] + y)
        if coordinates in seen_coordinates:
          overlapping_coordinates.add(coordinates)
        else:
          seen_coordinates.add(coordinates)
  return overlapping_coordinates

def part1(input_list):
  """ Find the number of grid coordinates that have overlapping claims """
  return len(generate_overlap(input_list))

def part2(input_list):
  """ ??? """
  overlap = generate_overlap(input_list)
  for claim in input_list:
    intact = True
    for x in range(1, claim['width']+ 1):
      for y in range(1, claim['height'] + 1):
        coordinates = (claim['left_margin'] + x, claim['top_margin'] + y)
        if coordinates in overlap:
          intact = intact and False
    if intact:
      return claim['id']



if __name__ == "__main__":
  assert part1(parse_input('inputs/day03_part1_test.txt')) == 4
  print(f"Part 1: {part1(parse_input('inputs/day03.txt'))}")

  assert part2(parse_input('inputs/day03_part1_test.txt')) == 3
  print(f"Part 2: {part2(parse_input('inputs/day03.txt'))}")
