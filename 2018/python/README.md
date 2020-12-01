# adventofcode_py_2018
My solutions to the 2018 Advent of Code challenge. A couple of notes on my approach:

1. Solve quickly, regardless of the ugliness or brute force nature of the approach.
2. Revisit and optimize.
3. Ensure tests and linters are passing.
4. Time permitting, GOTO 2

All solutions written in Python 3.7.1.

# Solution Callouts:

* Day 05: I learned a couple of things on this one. First, both the `re.sub` and `string.replace` methods are WAY faster at this kind of character removal than rebuilding strings using slices. (`string = string[4:] + string[:6]`) `string.replace` seemed to edge `re.sub` out on that front. Also, you can save a lot of time by using the reduced string from part 1 as your input, since it's not actually destroying any reaction opportunities.