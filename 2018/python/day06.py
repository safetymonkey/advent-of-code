"""Given a list of coordinates, find the region with the most and least space
between each of those coordinates.
Part 1: Find the region with the most space between coordinates.
Part 2: Find the region with the least space between coordinates.
https://adventofcode.com/2018/day/6
"""

# Imports
from collections import defaultdict
import re

# Helper/convenence methods
def parse_input(filename):
  """Convenience method to parse a file and return a list as input"""
  with open(filename, 'r') as input_file:
    coordinate_list, min_x, max_x, min_y, max_y = [], None, None, None, None
    for line in input_file:
      x, y = list(map(int, line.split(', ')))
      min_x = x if not min_x or x < min_x else min_x
      max_x = x if not max_x or x > max_x else max_x
      min_y = y if not min_y or y < min_y else min_y
      max_y = y if not max_y or y > max_y else max_y
      coordinate_list.append([x, y])
  return coordinate_list, min_x, max_x, min_y, max_y

def is_infinite(coord, min_x, max_x, min_y, max_y):
  if int(coord[0]) == min_x or int(coord[0]) == max_x or int(coord[1]) == min_y or int(coord[1]) == max_y:
    return True
  return False

def find_nearest(target, coordinate_list):
  distance_dict = {}
  for coordinate in coordinate_list:
    distance_dict[str(coordinate)] = abs(coordinate[0] - target[0]) + abs(coordinate[1] - target[1])
  shortest_two = sorted(list(distance_dict.values()))[:2]
  if len(set(shortest_two)) == 1:
     return None
  else:
    shortest = shortest_two[0]
    for coord, distance in distance_dict.items():
      if distance == shortest:
        return str(coord)

def in_range(target, coordinate_list, max_dist):
  """Identifies whether a given coordinate is within a provided distance of all target coords"""
  distance = 0
  for coordinate in coordinate_list:
    distance += abs(coordinate[0] - target[0]) + abs(coordinate[1] - target[1])
  return distance < max_dist

def part1(coordinate_list, min_x, max_x, min_y, max_y):
  """Find the number of coordinates closest to each target and return the biggest one."""
  area_dict = defaultdict(int)
  total_checked = 0
  for grid_x in range(min_x, max_x):
    for grid_y in range(min_y, max_y):
      area_dict[find_nearest([grid_x, grid_y], coordinate_list)] += 1
      total_checked += 1

  remove_list = []
  for coord in area_dict.keys():
    if coord is None:
      continue
    str_coord = str(re.sub(r'\[|\]', '', coord)).split(',')
    if is_infinite(str_coord, min_x, max_x, min_y, max_y):
      remove_list.append(coord)
  for remove in remove_list:
    del area_dict[remove]

  print(sorted(list(area_dict.values())))
  return max(list(area_dict.values()))

def part2(coordinate_list, max_dist, min_x, max_x, min_y, max_y):
  """Find the number of coordinates within a max distance of all target coordinates"""
  region = 0
  for grid_x in range(min_x, max_x):
    for grid_y in range(min_y, max_y):
      if in_range([grid_x, grid_y], coordinate_list, max_dist):
        region += 1
  return region

if __name__ == "__main__":
  INPUT = 'inputs/day06.txt'
  TEST_INPUT = 'inputs/day06_test.txt'

  coordinate_list, min_x, max_x, min_y, max_y = parse_input(TEST_INPUT)
  assert part1(coordinate_list, min_x, max_x, min_y, max_y) == 17
  coordinate_list, min_x, max_x, min_y, max_y = parse_input(INPUT)
  print(f"Part 1: {part1(coordinate_list, min_x, max_x, min_y, max_y)}")
  # NOTE: For some reason, my code works with the test but not input. Strangely,
  # the second highest value found was the correct answer. I'll try to come back
  # and solve this irregularity later. However, I know there was a bug with the
  # input for this day and I'm not sure if that's the root cause.

  coordinate_list, min_x, max_x, min_y, max_y = parse_input(TEST_INPUT)
  assert part2(coordinate_list, 32, min_x, max_x, min_y, max_y) == 16
  coordinate_list, min_x, max_x, min_y, max_y = parse_input(INPUT)
  print(f"Part 2: {part2(coordinate_list, 10000, min_x, max_x, min_y, max_y)}")