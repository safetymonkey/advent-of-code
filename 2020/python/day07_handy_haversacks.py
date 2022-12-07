"""
PUZZLE DESCRIPTION
Part 1: In a grouping of strings, find the number of characters that appear at least once
Part 2: In a grouping of strings, find the number of characters that appear in each item in the grouping

https://adventofcode.com/2020/day/7
"""

# Constants
DAY = '07'
INPUT = f"inputs/day{DAY}.txt"
TEST_INPUT = f"inputs/day{DAY}_test.txt"

# Imports
from _helpers import timer
from collections import defaultdict
import re


def parse_input(filename):
  """ Convenience method to parse input file """
  return open(filename, "r").read().splitlines()


@timer
def part1(filename):
  def get_parents(color, parent_dict):
    if color not in parent_dict.keys():
      return set(color)
    return {get_parents(target, parent_dict) for target in parent_dict[color]}

  input = parse_input(filename)
  r = re.compile(r'(\w+ \w+) bags?')
  rules = {}
  for line in input:
    matches = r.findall(line)
    rules[matches[0]] = matches[1:]
  parents = defaultdict(list)
  for parent, children in rules.items():
    for color in children:
      if color == 'no other':
        continue
      parents[color].append(parent)
  print(rules)
  print(parents)
  parent_set = get_parents('shiny gold', parents)
  print(parent_set)
  return len(rules)


@timer
def part2(input):
  count = 0
  for line in input:
    chars, total = line
    count += len([x for x in set(chars) if chars.count(x) == total])
  return count


if __name__ == "__main__":
  assert part1(TEST_INPUT) == 4
  print(f"Part 1: {part1(INPUT)}")
  print('\n')
  # assert part2(parse_input(TEST_INPUT)) == 6
  # print(f"Part 2: {part2(parse_input(INPUT))}")