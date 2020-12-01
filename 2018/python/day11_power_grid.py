"""Find the grouping of power cells with the most power
Part 1: Find the group of 3x3 power cells with the most power in a 300x300 grid
Part 2: Find the grouping of power cells with the most power when the group sizing is variable
https://adventofcode.com/2018/day11
"""

import numpy as np

SERIAL = 7672

# Helper/convenence methods
def calculate_power(x, y):
  """Callable function for numpy to determine the power at given coordinates"""
  rack_id = x + 10
  power = ((rack_id * y) + SERIAL) * rack_id
  return (power // 100 % 10) - 5

def build_grid():
  """Simple call to build a numpy 2D array"""
  return np.fromfunction(calculate_power, (300,300), dtype=int)

def find_maximum_power(grid_range):
  """Find the coordinates and grid size with the biggest cumulative power"""
  grid = build_grid()
  max_dict = {}
  for width in grid_range:
    windows = sum(grid[x:x-width+1 or None, y:y-width+1 or None] for x in range(width) for y in range(width))
    maximum = int(windows.max())
    location = np.where(windows == maximum)
    max_dict[maximum] = [location[0][0], location[1][0], width]
  print(max_dict[max(max_dict.keys())])

def part1():
  """Run the check once for width 3"""
  find_maximum_power(range(3,4))

def part2():
  """Run the check for every width between 3 and 300"""
  find_maximum_power(range(3,300))

if __name__ == "__main__":
  part1()
  part2()