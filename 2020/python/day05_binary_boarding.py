"""
PUZZLE DESCRIPTION
Part 1: Find the maximum seat number for a list encoded in binary
Part 2: Find the missing seat number in the provided sequence

https://adventofcode.com/2020/day/5
"""

# Constants
DAY = '05'
INPUT = f"inputs/day{DAY}.txt"
TEST_INPUT = f"inputs/day{DAY}_test.txt"

# Imports
from _helpers import timer


def parse_input(filename):
  """ Convenience method to parse input file """
  input = open(filename, "r").read().splitlines()
  return input


def parse_boarding_pass(input):
  row = int(input[0:7].replace('F', '0').replace('B', '1'), 2)
  column = int(input[7:10].replace('L', '0').replace('R', '1'), 2)
  seat = row * 8 + column
  return seat


@timer
def part1(input):
  seats = [parse_boarding_pass(line) for line in input]
  return max(seats)


@timer
def part2(input):
  seats = [parse_boarding_pass(line) for line in input]
  seats.sort()
  start, end = seats[0], seats[-1]
  return sorted(set(range(start, end + 1)).difference(seats))


if __name__ == "__main__":
  assert part1(['FBFBBFFRLR']) == 357
  print(f"Part 1: {part1(parse_input(INPUT))}")
  print('\n')
  print(f"Part 2: {part2(parse_input(INPUT))}")