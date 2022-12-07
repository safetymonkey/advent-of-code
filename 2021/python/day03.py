"""
PUZZLE DESCRIPTION
Part 1: ???
Part 2: ???

https://adventofcode.com/2020/day/X

Notes:
* ???
"""

# Constants
DAY = "03"

# Imports
from timer import timer
from collections import defaultdict, Counter


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


def get_most_and_least_common(input):
    counter_dict = defaultdict(Counter)
    input_lenth = len(input[0])
    for line in input:
        for i in range(input_lenth):
            counter_dict[i].update(line[i])

    most_common, least_common = "", ""
    for i in range(len(counter_dict)):
        mc = counter_dict[i].most_common(1)[0][0]
        lc = counter_dict[i].most_common()[::-1][0][0]
        if counter_dict[i]["0"] == counter_dict[i]["1"]:
            most_common += "1"
            least_common += "0"
        else:
            most_common += mc
            least_common += lc

    return most_common, least_common


def part1(input):
    most_common, least_common = get_most_and_least_common(input)

    output = int(most_common, 2) * int(least_common, 2)
    return output


def part2(input):
    oxygen_generator_rating, co2_scrubber_rating = input.copy(), input.copy()

    for i in range(len(oxygen_generator_rating[0])):
        most_common, _ = get_most_and_least_common(oxygen_generator_rating)
        oxygen_generator_rating = [
            line for line in oxygen_generator_rating if most_common[i] == line[i]
        ]
        if len(oxygen_generator_rating) == 1:
            break

    for i in range(len(co2_scrubber_rating[0])):
        _, least_common = get_most_and_least_common(co2_scrubber_rating)
        co2_scrubber_rating = [
            line for line in co2_scrubber_rating if least_common[i] == line[i]
        ]
        if len(co2_scrubber_rating) == 1:
            break

    output = int(oxygen_generator_rating[0], 2) * int(co2_scrubber_rating[0], 2)
    return output


if __name__ == "__main__":
    INPUT = f"inputs/day{DAY}.txt"
    TEST_INPUT = f"inputs/day{DAY}_test.txt"

    assert part1(parse_input(TEST_INPUT)) == 198
    print_output(1, parse_input(INPUT))

    # UNCOMMENT AFTER PART 1
    print("")
    assert part2(parse_input(TEST_INPUT)) == 230
    print_output(2, parse_input(INPUT))
