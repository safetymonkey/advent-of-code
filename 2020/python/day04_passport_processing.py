"""
PUZZLE DESCRIPTION
Part 1: Check a dictionary to validate it has all required keys.
Part 2: Check a dictionary to validate it has all required keys and values are valid.

https://adventofcode.com/2020/day/4
"""

# Constants
DAY = '04'
INPUT = f"inputs/day{DAY}.txt"
TEST_INPUT = f"inputs/day{DAY}_test.txt"
TEST_INPUT2 = f"inputs/day{DAY}_test2.txt"

REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

# Imports
from _helpers import timer
import re
from operator import itemgetter


def parse_input(filename):
  """ Convenience method to parse a file and return a list of dictionaries. """
  with open(filename) as f:
    input_list = f.readlines()
    input_list = [line.strip('\n') for line in input_list]

  # Colate dictionary values on different lines into a single string
  fixed_list, combined_str = [], ''
  for line in input_list:
    if line:
      combined_str += (line + ' ')
    else:
      combined_str.strip()
      fixed_list.append(combined_str)
      combined_str = ''
  fixed_list.append(combined_str)

  # Convert each string into a dictionary
  dict_list = []
  for line in fixed_list:
    temp_dict = {}
    for item in line.split(' '):
      if item:
        key, value = item.split(':')
        temp_dict[key] = value
    dict_list.append(temp_dict)

  return dict_list


@timer
def part1(input):
  """ Check a dictionary to validate it has all required keys. """
  valid = 0
  for item in input:
    if all(x in list(item) for x in REQUIRED_FIELDS):
      valid += 1
  return valid


def format_dict_list(dict_list):
  """ Convert dictionary values to their appropriate types. """
  dict_list['byr'] = int(dict_list['byr'])
  dict_list['iyr'] = int(dict_list['iyr'])
  dict_list['eyr'] = int(dict_list['eyr'])
  dict_list['hgt_int'] = int(
      dict_list['hgt'][:-2]) if dict_list['hgt'][:-2].isdigit() else 0
  dict_list['hgt_type'] = dict_list['hgt'][-2:]
  return dict_list


@timer
def part2(input):
  """ Check a dictionary to validate it has all required keys and values are valid. """
  valid = 0
  for item in input:
    if all(x in list(item) for x in REQUIRED_FIELDS):
      item = format_dict_list(item)
      if (item['byr'] in range(1920, 2003)) and \
        (item['iyr'] in range(2010, 2021)) and \
        (item['eyr'] in range(2020, 2031)) and \
        ((item['hgt_type'] == 'cm' and item['hgt_int'] in range(150,194)) or \
          (item['hgt_type'] == 'in' and item['hgt_int'] in range(59,77))) and \
        (re.match(r'^#[a-x0-9]{6}$', item['hcl']) and \
        (item['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']) and \
        (item['pid'].isdigit() and len(item['pid']) == 9) ):
        valid += 1
  return valid


if __name__ == "__main__":
  assert part1(parse_input(TEST_INPUT)) == 2
  print(f"Part 1: {part1(parse_input(INPUT))}")
  print('\n')
  assert part2(parse_input(TEST_INPUT2)) == 4
  print(f"Part 2: {part2(parse_input(INPUT))}")