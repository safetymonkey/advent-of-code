"""
PUZZLE DESCRIPTION
Part 1: Check a list of strings to see if a target character appears a certain number of times.
Part 2: Check a list of strings to see if a target character appears in exactly one of two locations.

https://adventofcode.com/2020/day/2
"""

# Constants
DAY = '02'
INPUT = f"inputs/day{DAY}.txt"
TEST_INPUT = f"inputs/day{DAY}_test.txt"

# Imports
from _helpers import timer
import re
from operator import itemgetter


def parse_input(filename):
  """Convenience method to parse a file and return a list as input"""
  with open(filename) as f:
    input_list = [re.split(r'\W', line) for line in f.readlines()]
  input_list = [[x for x in line if x] for line in input_list]
  return [tuple(line) for line in input_list]


@timer
def part1(input):
  """ Check a list of strings to see if a target character appears a certain number of times. """
  valid = 0
  for x in input:
    (min, max, letter, password) = x
    if password.count(letter) in range(int(min), int(max) + 1):
      valid += 1
  return valid


@timer
def part2(input):
  """ Check a list of strings to see if a target character appears in exactly one of two locations. """
  valid = 0
  for x in input:
    (pos1, pos2, letter, password) = x
    pos1, pos2 = int(pos1) - 1, int(pos2) - 1
    if (password[pos1] + password[pos2]).count(letter) == 1:
      valid += 1
  return valid


if __name__ == "__main__":
  assert part1(parse_input(TEST_INPUT)) == 2
  print(f"Part 1: {part1(parse_input(INPUT))}")
  print('\n')
  assert part2(parse_input(TEST_INPUT)) == 1
  print(f"Part 2: {part2(parse_input(INPUT))}")