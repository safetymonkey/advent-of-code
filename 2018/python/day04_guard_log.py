"""Find and exploit the (historically) sleepiest guard.
Part 1: Find guard who sleeps the most
Part 2: Find the guard who is most consistently asleep at a given minute
https://adventofcode.com/2018/day/4
"""

from collections import OrderedDict, defaultdict
import re

def parse_input(filename):
  """Convenience method to parse a file and return a list as input"""
  with open(filename, 'r') as input_file:
    activity_log = {}
    for line in input_file:
      match = re.match(r'\[(.*)\] (.*)', line)
      activity_log.update({match[1]: match[2]})
  return generate_guard_dict(OrderedDict(sorted(activity_log.items())))

def generate_guard_dict(activity_log):
  """Convert dict of activities into dict of minutes slept by guard"""
  guard_dict = defaultdict(list)
  guard, sleep_minute, awake_minute = 0, 0, 0
  for time, activity in activity_log.items():
    if 'begins shift' in activity:
      guard = re.findall(r'(\d+)', activity)[0]
    elif 'falls asleep' in activity:
      sleep_minute = get_minute(time)
    elif 'wakes up' in activity:
      awake_minute = get_minute(time)
      guard_dict[guard] += [i for i in range(sleep_minute, awake_minute)]
  return guard_dict

def get_minute(time_string):
  """Convenience method to ensure we're applying regex consistently"""
  return int(re.findall(r'\d{2}:(\d{2})', time_string)[0])

def find_sleepiest_minute(guard):
  """Find the minute that the given guard was asleep in most often"""
  minute_count = -1
  most_seen_minute = 0
  for i in range(60):
    if guard.count(i) > minute_count:
      minute_count = guard.count(i)
      most_seen_minute = i
  return most_seen_minute, guard.count(most_seen_minute)

def part1(guard_dict):
  """Strategy 1: Find the guard who sleeps the most overall."""
  most_slept = 0
  for sleepy_guard, slept in guard_dict.items():
    if len(slept) > most_slept:
      most_slept = len(slept)
      sleepiest_guard = sleepy_guard
  most_seen_minute = find_sleepiest_minute(guard_dict[sleepiest_guard])[0]
  return int(sleepiest_guard) * most_seen_minute

def part2(guard_dict):
  """Strategy 2: Find the guard who is most consistently asleep at the same time"""
  guard_id, most_seen_minute, most_seen_minute_frequency = 0, -1, 0
  for guard, slept in guard_dict.items():
    sleepiest_minute, minute_count = find_sleepiest_minute(slept)
    if minute_count > most_seen_minute_frequency:
      most_seen_minute_frequency = minute_count
      most_seen_minute = sleepiest_minute
      guard_id = guard
  return int(guard_id) * most_seen_minute

if __name__ == "__main__":
  INPUT = 'inputs/day04.txt'
  TEST_INPUT = 'inputs/day04_test.txt'

  assert part1(parse_input(TEST_INPUT)) == 240
  print(f"Part 1: {part1(parse_input(INPUT))}")

  assert part2(parse_input(TEST_INPUT)) == 4455
  print(f"Part 2: {part2(parse_input(INPUT))}")
