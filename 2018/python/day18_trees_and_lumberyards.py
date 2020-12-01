"""A modified game of Life with open fields, trees, and lumberyards
Part 1: Find score (# of trees * # of lumberyards) after 10 iterations.
Part 2: Find score after 1000000000 iterations.
https://adventofcode.com/2018/day/18
"""

# Imports
from collections import defaultdict

# Helper/convenence methods
def parse_input(filename, grid_size):
  """Convenience method to parse a file and return a 2D list as input"""
  grid = []
  with open(filename, 'r') as input_file:
    margin = get_margin(grid_size)
    grid.append(margin)
    for line in input_file:
      grid.append([' '] + [x for x in line.strip()] + [' '])
    grid.append(margin)
  return grid

def get_margin(grid_size):
  """Calculate the empty margin to put at the top and bottom of grids"""
  margin = [' ']
  margin *= grid_size + 2
  return margin

def get_neighbors(grid, row_number, column_number):
  """Check all neighboring cells and get a dictionary count of values"""
  neighbors_dict = defaultdict(int)
  for i in range(row_number - 1, row_number + 2):
    for j in range(column_number - 1, column_number + 2):
      if i == row_number and j == column_number:
        continue
      # print(f"i: {i} || j: {j}")
      cell = grid[i][j]
      if cell == '.':
        neighbors_dict['open'] += 1
      elif cell == '|':
        neighbors_dict['trees'] += 1
      elif cell == '#':
        neighbors_dict['lumberyard'] += 1
  return neighbors_dict

def advance_grid(grid):
  """Advance the grid one iteration"""
  margin = get_margin(len(grid))
  next_grid = [margin]
  for i in range(1, len(grid) - 1):
    next_grid.append([' '])
    for j in range(1, len(grid) - 1):
      neighbors = get_neighbors(grid, i, j)
      if grid[i][j] == '.' and neighbors['trees'] >= 3:
        next_grid[i].append('|')
      elif grid[i][j] == '.':
        next_grid[i].append(grid[i][j])

      if grid[i][j] == '|' and neighbors['lumberyard'] >= 3:
        next_grid[i].append('#')
      elif grid[i][j] == '|':
        next_grid[i].append(grid[i][j])

      if grid[i][j] == '#' and neighbors['trees'] >= 1 and neighbors['lumberyard'] >= 1:
        next_grid[i].append('#')
      elif grid[i][j] == '#':
        next_grid[i].append('.')
    next_grid[i].append(' ')
  next_grid.append(margin)
  return next_grid

def get_score(grid):
  """Given a grid, calcuate the score of trees * lumberyards"""
  lumberyards, trees = 0, 0
  for line in grid:
    for cell in line:
      if cell == '#':
        lumberyards += 1
      elif cell == '|':
        trees += 1
  return trees * lumberyards

def part1(grid):
  """Advance the grid 10 times, return the score"""
  for i in range(10):
    grid = advance_grid(grid)
  return get_score(grid)

def part2(grid):
  """Find score after 1000000000 iterations. The patterns begin to repeat, so
     the trick is to figure out the period of your repetition and then find the
     value that is at the modulo of that period.
  """
  previously_seen, new_grid = {}, []
  for i in range(1000000000):
    new_grid = advance_grid(grid)
    if new_grid not in list(previously_seen.values()):
      previously_seen[i] = list(new_grid)
      grid = new_grid
    else:
      break
  current_i, period = max(list(previously_seen.keys())), 0
  for k, v in previously_seen.items():
    if v == new_grid:
      period = current_i - k
  grid = new_grid

  for i in range(1000000000 % period):
    grid = advance_grid(grid)
  return get_score(grid)

if __name__ == "__main__":
  INPUT = 'inputs/day18.txt'
  TEST_INPUT = 'inputs/day18_test.txt'

  assert part1(parse_input(TEST_INPUT, 10)) == 1147
  print(f"Part 1: {part1(parse_input(INPUT, 50))}")
  print(f"Part 2: {part2(parse_input(INPUT, 50))}")