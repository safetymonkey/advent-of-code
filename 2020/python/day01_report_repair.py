"""
PUZZLE DESCRIPTION
Part 1: Find two integers that sum to 2020 and then multiply those two numbers
        together.
Part 2: Find three integers that sum to 2020 and then multiply those two numbers
        together.

https://adventofcode.com/2020/day/1

Could be improved by writing recursive functions to find N integers that add up
to TARGET_SUM
"""

# Constants
DAY = '01'
TARGET_SUM = 2020

# Imports
import functools
import time


# Helper/convenence methods
def timer(func):
  @functools.wraps(func)
  def wrapper_timer(*args, **kwargs):
    tic = time.perf_counter()
    value = func(*args, **kwargs)
    toc = time.perf_counter()
    elapsed_time = toc - tic
    print(f"Elapsed time: {elapsed_time:0.4f} seconds")
    return value

  return wrapper_timer


def parse_input(filename):
  """Convenience method to parse a file and return a list as input"""
  with open(filename, 'r') as input_file:
    input_array = [int(line) for line in input_file]
    return input_array


@timer
def part1(input):
  """ Find two integers that sum to 2020 and then multiply those two numbers together. """
  for i, i_value in enumerate(input):
    if i_value > TARGET_SUM:
      continue

    for j in range(i, len(input)):
      j_value = input[j]
      if i_value + j_value == TARGET_SUM:
        return (i_value * j_value)


@timer
def part2(input):
  """ Find three integers that sum to 2020 and then multiply those two numbers together. """
  for i, i_value in enumerate(input):
    if i_value > TARGET_SUM:
      continue

    for j in range(i, len(input)):
      j_value = input[j]
      if i_value + j_value <= TARGET_SUM:
        for k in range(j, len(input)):
          k_value = input[k]
          if i_value + j_value + k_value == TARGET_SUM:
            return (i_value * j_value * k_value)


if __name__ == "__main__":
  INPUT = f"inputs/day{DAY}.txt"
  TEST_INPUT = f"inputs/day{DAY}_test.txt"

  assert part1(parse_input(TEST_INPUT)) == 514579
  print(f"Part 1: {part1(parse_input(INPUT))}")

  print('\n')

  assert part2(parse_input(TEST_INPUT)) == 241861950
  print(f"Part 2: {part2(parse_input(INPUT))}")