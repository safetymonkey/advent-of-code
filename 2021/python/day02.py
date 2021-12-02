"""
PUZZLE DESCRIPTION
Part 1: ???
Part 2: ???

https://adventofcode.com/2020/day/X

Notes:
* ???
"""

# Constants
DAY = "02"

# Imports
from timer import timer


def parse_input(filename):
    """Convenience method to parse a file and return a list as input"""
    with open(filename, "r") as input_file:
        # RAW
        input_array = [line.rstrip() for line in input_file]
        return input_array


@timer
def print_output(part: int, input: list):
    """Convenience method to print output to console"""
    if part == 1:
        output = part1(input)
        print(f"Part 1: {output}")
    elif part == 2:
        output = part2(input)
        print(f"Part 2: {output}")


def part1(input):
    horizontal_sum, depth_sum = 0, 0
    for line in input:
        direction, distance = line.split(" ")
        if direction == "forward":
            horizontal_sum += int(distance)
        elif direction == "up":
            depth_sum -= int(distance)
        elif direction == "down":
            depth_sum += int(distance)

    output = horizontal_sum * depth_sum
    return output


def part2(input):
    aim, horizontal_sum, depth_sum = 0, 0, 0
    for line in input:
        direction, distance = line.split(" ")
        if direction == "forward":
            horizontal_sum += int(distance)
            depth_sum += int(distance) * aim
        elif direction == "up":
            aim -= int(distance)
        elif direction == "down":
            aim += int(distance)

    return horizontal_sum * depth_sum


if __name__ == "__main__":
    INPUT = f"inputs/day{DAY}.txt"
    TEST_INPUT = f"inputs/day{DAY}_test.txt"

    assert part1(parse_input(TEST_INPUT)) == 150
    print_output(1, parse_input(INPUT))

    print("\n")
    assert part2(parse_input(TEST_INPUT)) == 900
    print_output(2, parse_input(INPUT))
