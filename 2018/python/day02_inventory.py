"""Find two boxes with similar IDs in a warehouse.
Part 1: Generate a checksum based on character counts in the box IDs
Part 2: Find the two box IDs that have all but one character in common
https://adventofcode.com/2018/day/2
"""

def parse_input(filename):
  """Convenience method to parse a file and return a list as input"""
  with open(filename, 'r') as input_file:
    return [i.rstrip() for i in input_file]

def part1(input_string):
  """Generate checksum by evaluating character counts in input strings"""
  twos, threes = 0, 0
  for line in input_string:
    letters_seen = {}
    for char in line:
      letters_seen[char] = letters_seen.setdefault(char, 0)+1
    if 2 in letters_seen.values():
      twos += 1
    if 3 in letters_seen.values():
      threes += 1
  return threes * twos

def part2(input_string):
  """Find two strings in the list who have all but one character in common"""
  length = len(input_string[0])
  for i in range(length):
    modified_input = [line[:i] + line[i+1:] for line in input_string]
    for line in modified_input:
      if modified_input.count(line) == 2:
        return line

if __name__ == "__main__":
  assert part1(parse_input('inputs/day02_part1_test.txt')) == 12
  print(f"Part 1: {part1(parse_input('inputs/day02.txt'))}")

  assert part2(parse_input('inputs/day02_part2_test.txt')) == 'fgij'
  print(f"Part 2: {part2(parse_input('inputs/day02.txt'))}")
