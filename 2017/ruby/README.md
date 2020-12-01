# adventofcode_rb_2017

My personal crack at [Advent of Code](http://adventofcode.com). My focus in competing was in this order:

1. **Readability**.
2. **Simplicity**.
3. **Minimalization**.
4. **Speed of execution**.

All solutions are written in Ruby 2.4.x.

# Input

In general, all solutions can be invoked without command-line arguments.
Doing so runs the code on the input corresponding with my user.
This means that to run the solution for a given day, it should suffice to type `ruby <day><tab><enter>`.

Most scripts will use my user-specific input.
Command-line interaction is possible to specify alternates.

# Highlights

Interesting learnings from the exercise:

* 05 (CPU jumps):
  My code wasn't initially rendering the correct response for part 2, even though the logic was correct. What I didn't realize is that passing my input array into the solution methods mutated the contents of the array without my realizing it. The better solution was to pass in a clone of the array.

If you like, you may browse my 2016 solutions here:
* [Ruby](https://github.com/safetymonkey/adventofcode_rb_2016)

In the interest of credit, I took a fair deal of inspiration (and much of this README) from [petertseng](https://github.com/petertseng/adventofcode-rb-2017).