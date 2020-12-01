"""Map how plants spread through infinite pots over time
Part 1: What's the sum of filled pots after 20 iterations?
Part 2: What's the sum of filled pots after 50 billion iterations?
https://adventofcode.com/2018/day/12
"""

# Helper/convenence methods
def parse_input(filename):
  """Convenience method to parse a file and return a list as input"""
  rules = {}
  with open(filename, 'r') as input_file:
    initial_state = [x for x in input_file.readline().split(' ')[2].strip()]
    for line in input_file:
      if line == '\n':
        continue
      line = line.strip().split(' ')
      rules[line[0]] = line[2]
  return initial_state, rules

def get_next_pots(pots, first_pot, rules):
  """Return the next iteration of pots based on rules provided"""
  next_pots = []
  for i in range(len(pots)):
    if i == 0:
      sample = '..' + ''.join(pots[0:3])
    elif i == 1:
      sample = '.' + ''.join(pots[0:4])
    elif i == len(pots) - 1:
      sample = ''.join(pots[i - 2:i + 1]) + '..'
    elif i == len(pots) - 2:
      sample = ''.join(pots[i - 2:i + 2]) + '.'
    else:
      sample = ''.join(pots[i - 2:i + 3])
    if sample in rules.keys():
      next_pots.append(rules[sample])
    else:
      next_pots.append('.')
  if '#' in next_pots[-2:]:
    next_pots += ['.', '.']
  if '#' in next_pots[0:2]:
    first_pot -= 2
    pots = ['.', '.'] + next_pots
  else:
    pots = next_pots
  return pots, first_pot

def pots_sum(pots, first_pot):
  """Return the sum of the numbers of the filled pots"""
  sum = 0
  for idx, value in enumerate(pots):
    if value == '#':
      sum += idx + first_pot
  return sum

def part1(filename, times):
  """Returns the sum of filled pots after 20 iterations"""
  pots, rules = parse_input(filename)
  first_pot = -3
  pots = (['.'] * 3) + pots + (['.'] * 15)
  for _ in (range(times)):
    pots, first_pot = get_next_pots(pots, first_pot, rules)
  return pots_sum(pots, first_pot)

def part2(filename, times):
  """Returns the sum of filled pots after 50 billion iterations by identifying
     when the pattern begins to repeat and calculating the future value off the
     consistent delta
  """
  pots, rules = parse_input(filename)
  pots = (['.'] * 3) + pots + (['.'] * 15)
  first_pot, deltas = -3, []
  for i in range(times):
    original_sum = pots_sum(pots, first_pot)
    next_pots, first_pot = get_next_pots(pots, first_pot, rules)
    deltas.append(pots_sum(next_pots, first_pot) - original_sum)
    if len(deltas) > 10 and len(set(deltas[-5:])) == 1:
      return ((times - (i + 1)) * deltas[-1]) + pots_sum(next_pots, first_pot)
    pots = next_pots

if __name__ == "__main__":
  INPUT = 'inputs/day12.txt'
  TEST_INPUT = 'inputs/day12_test.txt'

  assert part1(TEST_INPUT, 20) == 325
  print(f"Part 1: {part1(INPUT, 20)}")

  print(f"Part 2: {part2(INPUT, 50000000000)}")
