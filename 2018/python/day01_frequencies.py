"""Find a final value after combining a long string of changes"""

def part1(input_string):
  """Since beginning frequency == 0, return sum of changes"""
  return sum(input_string)

def part2(input_string):
  """Finds the first time a frequency is seen twice"""
  frequency = 0
  history = {0}
  i = 0
  while True:
    if i == len(input_string):
      i = 0
    frequency += input_string[i]
    if frequency in history:
      return frequency
    i += 1
    history.add(frequency)

if __name__ == "__main__":
  with open('inputs/day01.txt', 'r') as input_file:
    INPUT = [int(i.rstrip()) for i in input_file]

  assert part1([1, -2, 3, 1]) == 3
  assert part1([1, +1, 1]) == 3
  assert part1([1, 1, -2]) == 0
  assert part1([-1, -2, -3]) == -6
  print(f"Part 1: {str(part1(INPUT))}")

  assert part2([1, -1]) == 0
  assert part2([1, -2, 3, 1]) == 2
  assert part2([3, 3, 4, -2, -4]) == 10
  assert part2([-6, 3, 8, 5, -6]) == 5
  assert part2([7, 7, -2, -7, -4]) == 14
  print(f"Part 2: {str(part2(INPUT))}")
