"""Two elves are making hot chocolate, and there's a scoring system, and they
   make new recipes, and... look, the description is weird.
Part 1: Find the 10 scores after a certain number of iterations
Part 2: Find how many iterations it takes to produce a sequence of scores
https://adventofcode.com/2018/day/14
"""

def part1(puzzle_input):
  """Find the 10 scores after a certain number of iterations"""
  puzzle_input = int(puzzle_input)
  scores = [3, 7]
  elf1, elf2 = 0, 1
  while len(scores) < puzzle_input + 10:
    new_recipe = scores[elf1] + scores[elf2]
    scores.extend(divmod(new_recipe, 10) if new_recipe >= 10 else (new_recipe,))
    elf1 = (elf1 + 1 + scores[elf1]) % len(scores)
    elf2 = (elf2 + 1 + scores[elf2]) % len(scores)
  return ''.join(str(x) for x in scores[-10:])

def part2(puzzle_input):
  """Find how many iterations it takes to produce a sequence of scores"""
  scores = [3, 7]
  elf1, elf2 = 0, 1
  puzzle_input = [int(i) for i in puzzle_input]
  while scores[-(len(puzzle_input)):] != puzzle_input and \
        scores[-(len(puzzle_input))-1:-1] != puzzle_input:
    new_recipe = scores[elf1] + scores[elf2]
    scores.extend(divmod(new_recipe, 10) if new_recipe >= 10 else (new_recipe,))
    elf1 = (elf1 + 1 + scores[elf1]) % len(scores)
    elf2 = (elf2 + 1 + scores[elf2]) % len(scores)
  return len(scores) - len(puzzle_input) - (0 if scores[-len(puzzle_input):] == puzzle_input else 1)

if __name__ == "__main__":
  INPUT = '074501'

  assert part1('9') == '5158916779'
  print(f"Part 1: {part1(INPUT)}")

  assert part2('51589') == 9
  assert part2('01245') == 5
  assert part2('92510') == 18
  assert part2('59414') == 2018
  print(f"Part 2: {part2(INPUT)}")
