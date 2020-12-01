"""Figure out the best plan to complete a list of steps with 1-to-many dependancies.
Part 1: Find the order the steps will be completed if you do it by yourself.
Part 2: Find the time it will take to complete if each step has an associated
        time and you have some helpers.
https://adventofcode.com/2018/day/7
"""

# Imports
import re
from collections import defaultdict

# Helper/convenence methods
def parse_input(filename):
  """Convenience method to parse a file and return a list as input"""
  steps_dict = defaultdict(list)
  with open(filename, 'r') as input_file:
    for line in input_file:
      match = re.match(r'Step (\w) must be finished before step (\w) can begin.', line)
      steps_dict[match[1]].append(match[2])
  return steps_dict

def complete_time(char, offset):
  """Find the amount of time to complete a given step (or character)"""
  return ord(char.lower()) - 96 + offset

def find_dependencies(input_dict):
  """Review the steps to create a list of steps that are blocked and unblocked"""
  blocked = []
  for blockers in input_dict.values():
    blocked += blockers
  unblocked = [x for x in list(input_dict.keys()) if x not in blocked]
  return blocked, unblocked

def part1(input_dict):
  """Find the order the steps will be completed in if you work by yourself."""
  order = []
  blocked, unblocked = find_dependencies(input_dict)
  while bool(unblocked):
    completed = min(unblocked)
    for i in input_dict[completed]:
      if i in blocked:
        blocked.remove(i)
      if i not in blocked:
        unblocked.append(i)
    unblocked.remove(completed)
    order.append(completed)
  return ''.join(order)

def part2(input_dict, max_workers, offset):
  """Find the time you will finish work if steps take time and you have help."""
  workers, time, completed, completion_dict = 0, 0, [], defaultdict(list)
  blocked, unblocked = find_dependencies(input_dict)
  while blocked or unblocked:
    if time in completion_dict:
      for j in completion_dict[time]:
        for i in input_dict[j]:
          if i in blocked:
            blocked.remove(i)
          if i not in blocked:
            unblocked.append(i)
        workers -= 1
        completed.append(j)
    for i in range(len(unblocked)):
      if workers < max_workers and unblocked:
        workers += 1
        step = min(unblocked)
        will_complete = complete_time(min(unblocked), offset) + time
        completion_dict[will_complete].append(step)
        unblocked.remove(step)
    time += 1
  return will_complete

if __name__ == "__main__":
  INPUT = 'inputs/day07.txt'
  TEST_INPUT = 'inputs/day07_test.txt'

  assert part1(parse_input(TEST_INPUT)) == 'CABDFE'
  print(f"Part 1: {part1(parse_input(INPUT))}")

  assert complete_time('Z', 60) == 86
  assert part2(parse_input(TEST_INPUT), 2, 0) == 15
  print(f"Part 2: {part2(parse_input(INPUT), 5, 60)}")
