"""
PUZZLE DESCRIPTION
Part 1: ???
Part 2: ???

https://adventofcode.com/2020/day/8
"""

# Constants
DAY = '08'
INPUT = f"inputs/day{DAY}.txt"
TEST_INPUT = f"inputs/day{DAY}_test.txt"

# Imports
from _helpers import timer


def parse_input(filename):
  """ Convenience method to parse input file """
  return open(filename, "r").read().splitlines()


def parse_line(line):
  command, next_int = line.split()
  next_int = int(next_int)
  return command, next_int


def traverse_instructions(input, i=0, visited=[], swap=False):
  acc, visited = 0, []
  while (i not in visited) and i < len(input):
    visited.append(i)
    command, next_int = parse_line(input[i])
    if command == 'jmp':
      i += next_int
      continue
    if command == 'acc':
      acc += next_int
    i += 1
  return acc, visited, (i not in visited)


@timer
def part1(input):
  acc, visited, _ = traverse_instructions(input)
  return acc, visited


@timer
def part2(input, visited):
  acc = 0
  # for i, line in enumerate(input):
  for i in visited:
    command, next_int = parse_line(input[i])
    if command != 'acc':
      clone = input.copy()
      if command == 'nop':
        clone[i] = clone[i].replace('nop', 'jmp')
      elif command == 'jmp':
        clone[i] = clone[i].replace('jmp', 'nop')
      acc, _, complete = traverse_instructions(clone)
      if complete:
        break
  return acc


if __name__ == "__main__":
  acc, visited_test = part1(parse_input(TEST_INPUT))
  assert acc == 5
  acc, visited = part1(parse_input(INPUT))
  print(f"Part 1: {acc}")
  print('\n')
  assert part2(parse_input(TEST_INPUT), visited_test) == 8
  print(f"Part 2: {part2(parse_input(INPUT), visited)}")