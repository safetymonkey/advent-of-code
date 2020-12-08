"""
PUZZLE DESCRIPTION
Part 1: In a grouping of strings, find the number of characters that appear at least once
Part 2: In a grouping of strings, find the number of characters that appear in each item in the grouping

https://adventofcode.com/2020/day/6
"""

# Constants
DAY = '06'
INPUT = f"inputs/day{DAY}.txt"
TEST_INPUT = f"inputs/day{DAY}_test.txt"

# Imports
from _helpers import timer


def parse_input(filename):
  """ Convenience method to parse input file """
  input = open(filename, "r").read().splitlines()
  collated, temp_str, count = [], '', 0
  for line in input:
    if not line:
      collated.append((temp_str, count))
      temp_str = ''
      count = 0
    else:
      temp_str += line
      count += 1
  collated.append((temp_str, count))
  return collated


@timer
def part1(input):
  counts = [len(''.join(set(line[0]))) for line in input]
  return sum(counts)


@timer
def part2(input):
  count = 0
  for line in input:
    chars, total = line
    count += len([x for x in set(chars) if chars.count(x) == total])
  return count


if __name__ == "__main__":
  assert part1(parse_input(TEST_INPUT)) == 11
  print(f"Part 1: {part1(parse_input(INPUT))}")
  print('\n')
  assert part2(parse_input(TEST_INPUT)) == 6
  print(f"Part 2: {part2(parse_input(INPUT))}")