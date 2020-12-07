"""
PUZZLE DESCRIPTION
Part 1: Find the number of trees ('#') encountered on a given slope.
Part 2: Find the multiplied value of all the trees on several slopes.

https://adventofcode.com/2020/day/3
"""

# Constants
DAY = '03'
INPUT = f"inputs/day{DAY}.txt"
TEST_INPUT = f"inputs/day{DAY}_test.txt"

# Imports
from _helpers import timer
from functools import reduce


def parse_input(filename):
  """ Convenience method to parse a file and return a list of dictionaries. """
  #   with open(filename) as f:
  #     input_list = f.readlines()
  #     input_list = [line.strip('\n') for line in input_list]
  #   return dict_list
  input = open(filename, "r").read().splitlines()
  input = [line * len(input) for line in input]
  return input


def check_slope(x, y, input):
  trees, i = 0, 0
  while i * x < len(input):
    if input[x * i][y * i] == '#':
      trees += 1
    i += 1
  return trees


@timer
def part1(input):
  """ Find the number of trees ('#') encountered on a given slope. """
  return check_slope(1, 3, input)


@timer
def part2(input):
  """ Find the multiplied value of all the trees on several slopes. """
  slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
  return reduce((lambda x, y: x * y),
                [check_slope(*slope, input) for slope in slopes])


if __name__ == "__main__":
  assert part1(parse_input(TEST_INPUT)) == 7
  print(f"Part 1: {part1(parse_input(INPUT))}")
  print('\n')
  assert part2(parse_input(TEST_INPUT)) == 336
  print(f"Part 2: {part2(parse_input(INPUT))}")