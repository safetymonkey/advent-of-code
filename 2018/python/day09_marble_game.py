"""The Marble Game
Part 1: Find who has the highest score for a given total number of marbles
Part 2: Same as above, but the number of marbles is 100x longer
https://adventofcode.com/2018/day/9
"""

# Imports
from collections import deque, defaultdict

# Helper/convenence methods
def parse_input(input_string):
  """Parse input string into three keyed values"""
  input_array = input_string.split()
  players, last_marble = int(input_array[0]), int(input_array[6])
  expected_answer = int(input_array[-1]) if len(input_array) > 9 else None
  return players, last_marble, expected_answer

def play_game(input_string, part2=False):
  """Play the marble game and return the high score"""
  player_count, last_marble, expected_answer = parse_input(input_string)
  i, player = 0, 0
  if part2:
    last_marble *= 100
  circle = deque([0])
  player_score = defaultdict(int)
  while i <= last_marble:
    i += 1
    player = (player % player_count) + 1
    if i % 23 != 0:
      circle.rotate(-2)
      circle.append(i)
      circle.rotate(1)
    else:
      circle.rotate(7)
      player_score[player] += i + circle.popleft()
  if expected_answer:
    assert expected_answer == max(player_score.values())
  else:
    return max(player_score.values())

if __name__ == "__main__":
  INPUT = open('inputs/day09.txt').readline()
  TEST_INPUT = '10 players; last marble is worth 1618 points: high score is 8317'

  play_game(TEST_INPUT)
  print(f"Part 1: {play_game(INPUT)}")
  print(f"Part 2: {play_game(INPUT, True)}")
