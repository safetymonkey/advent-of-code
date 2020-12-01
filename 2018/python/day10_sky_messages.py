"""Lights are moving in the sky. Find out when they converge to form a message!
Part 1: Identify the message from the first time the lights form a coherent string.
Part 2: Identify how long you'd have to wait to see that message.
https://adventofcode.com/2018/day/10
"""

# Imports
import re

class Light():
  """A Simple class to handle the lights and their current/next position"""
  def __init__(self, input_data):
    self.x_coord = input_data[0]
    self.y_coord = input_data[1]
    self.x_veloc = input_data[2]
    self.y_veloc = input_data[3]

  def get_coords(self):
    """Return a list of the current coordinates"""
    return [self.x_coord, self.y_coord]

  def get_next_coords(self):
    """Return a list of the NEXT coordinates"""
    return [self.x_coord + self.x_veloc, self.y_coord + self.y_veloc]

  def update(self):
    """Update the object to the next coordinates"""
    self.x_coord += self.x_veloc
    self.y_coord += self.y_veloc

def parse_input(filename):
  """Convenience method to parse a file and return a list of Light objects"""
  lights = []
  with open(filename, 'r') as input_file:
    for line in input_file:
      light = Light(list(map(int, re.findall(r'(-?\d+)', line))))
      lights.append(light)
  return lights

def print_lights(lights):
  """Print the current visible lights on the screen"""
  light_coords, x_coords, y_coords = [], [], []
  min_x, max_x, min_y, max_y = None, None, None, None

  for light in lights:
    coord = light.get_coords()
    x_coords.append(coord[0])
    y_coords.append(coord[1])
    light_coords.append(coord)

  min_x, max_x = min(x_coords), max(x_coords)
  min_y, max_y = min(y_coords), max(y_coords)

  for y_coord in range(min_y, max_y + 1):
    for x_coord in range(min_x, max_x + 1):
      print('# ' if [x_coord, y_coord] in light_coords else '. ', end='')
    print('')

def get_area_size(lights, next_area=False):
  """Return the total area size of the lights. If Next == True, get the NEXT coords"""
  min_x, max_x, min_y, max_y = None, None, None, None
  for light in lights:
    coord = light.get_coords() if not next_area else light.get_next_coords()
    min_x = coord[0] if not min_x or coord[0] < min_x else min_x
    min_y = coord[1] if not min_x or coord[1] < min_x else min_x
    max_x = coord[0] if not max_x or coord[0] > max_x else max_x
    max_y = coord[1] if not max_x or coord[1] > max_x else max_x
  return abs(max_x - min_x) * abs(max_y - min_y)

def part1(lights):
  """This actually does double duty for both parts. Iterate lights until they
  hit their smallest area
  """
  i = 0
  while True:
    area = get_area_size(lights)
    next_area = get_area_size(lights, True)
    if next_area >= area:
      print(f"Iteration #{i}:")
      print_lights(lights)
      return
    for light in lights:
      light.update()
    i += 1

if __name__ == "__main__":
  INPUT = 'inputs/day10.txt'
  TEST_INPUT = 'inputs/day10_test.txt'

  part1(parse_input(TEST_INPUT))
  part1(parse_input(INPUT))
