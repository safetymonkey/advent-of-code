"""
PUZZLE DESCRIPTION
Part 1: ???
Part 2: ???

https://adventofcode.com/2020/day/X

Notes:
* ???
"""

# Constants
DAY = '00'

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
    # RAW
    # input_array = [int(line) for line in input_file]
    # return input_array

    # REGEX (requires import)
    # for line in input_file:
    #   match = re.match(r'\[(.*)\] (.*)', line)
    # return X


@timer
def part1(input):
  return


@timer
def part2(input):
  return


if __name__ == "__main__":
  INPUT = f"inputs/day{DAY}.txt"
  TEST_INPUT = f"inputs/day{DAY}_test.txt"

  assert part1(parse_input(TEST_INPUT)) == 514579
  print(f"Part 1: {part1(parse_input(INPUT))}")

  # UNCOMMENT AFTER PART 1
  # print('\n')
  # assert part2(parse_input(TEST_INPUT)) == 241861950
  # print(f"Part 2: {part2(parse_input(INPUT))}")
