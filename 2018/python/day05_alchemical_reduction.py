"""Reduce the size of a polymer strand
Part 1: Remove all ooposite polarities (capitalizations) from the string to find
        the shortest possible length
Part 2: Try removing each character in the alphabet from the polymer string
        before reducing to find another shortest possible length
https://adventofcode.com/2018/day/5
"""

# Imports
from string import ascii_lowercase
import re

# Helper/convenence methods
def parse_input(filename):
  """Convenience method to parse a file and return a list as input"""
  with open(filename, 'r') as input_file:
    return input_file.readline()

def try_reaction(input_string):
  """Remove all instances of two adjacent characters of diff. capitalizations"""
  for char in ascii_lowercase:
    input_string = re.sub(char.lower() + char.upper(), '', input_string)
    input_string = re.sub(char.upper() + char.lower(), '', input_string)
  return input_string

def part1(input_string):
  """Remove all ooposite polarities (capitalizations) from the string to find
     the shortest possible length
  """
  while True:
    new_input = try_reaction(input_string)
    if new_input == input_string:
      return len(input_string)
    input_string = new_input

def part2(input_string):
  """Try removing each character in the alphabet from the polymer string
     before reducing to find another shortest possible length
  """
  test_input = ""
  shortest_value = len(input_string)
  for char in ascii_lowercase:
    test_input = input_string.replace(char, '').replace(char.upper(), '')
    length = part1(test_input)
    if length < shortest_value:
      shortest_value = length
  return shortest_value

if __name__ == "__main__":
  INPUT = 'inputs/day05.txt'
  TEST_INPUT = 'dabAcCaCBAcCcaDA'

  assert part1(TEST_INPUT) == 10
  print(f"Part 1: {str(part1(parse_input(INPUT)))}")

  assert part2(TEST_INPUT) == 4
  print(f"Part 2: {part2(parse_input(INPUT))}")
