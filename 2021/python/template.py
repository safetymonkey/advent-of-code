"""
PUZZLE DESCRIPTION
Part 1: ???
Part 2: ???

https://adventofcode.com/2020/day/X

Notes:
* ???
"""

# Constants
DAY = "00"

# Imports
from timer import timer


def parse_input(filename):
    """Convenience method to parse a file and return a list as input"""
    with open(filename, "r") as input_file:
        # RAW
        # input_array = [int(line) for line in input_file]
        # return input_array

        # REGEX (requires import)
        # for line in input_file:
        #   match = re.match(r'\[(.*)\] (.*)', line)
        # return X
        return


@timer
def print_output(part: int, input: list):
    """Convenience method to print output to console"""
    if part == 1:
        output = part1(input)
        print(f"Part 1: {output}")
    elif part == 2:
        output = part2(input)
        print(f"Part 2: {output}")


@timer
def part1(input):
    output = None
    return output


@timer
def part2(input):
    output = None
    return output


if __name__ == "__main__":
    INPUT = f"inputs/day{DAY}.txt"
    TEST_INPUT = f"inputs/day{DAY}_test.txt"

    assert part1(parse_input(TEST_INPUT)) == 150
    print_output(1, parse_input(INPUT))

    # UNCOMMENT AFTER PART 1
    # print('\n')
    # assert part2(parse_input(TEST_INPUT)) == 900
    # print_output(2, parse_input(INPUT))
