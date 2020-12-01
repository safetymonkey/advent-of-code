# Advent of Code typescript

Advent of Code Template using Node TS for Current Year.

Forked from [johnbeech's repo](https://github.com/johnbeech/advent-of-code-nodejs-template)

## Setup

If using the Advent of Code Template repo; click [**`Use this template`**](https://github.com/MJGTwo/advent-of-code-nodets-template/generate) and set a new repository name.

Clone this repo, then run `yarn install` to install dependencies.

If this a brand new repository, run: `ts-node setup` to configure it for Current Year and check in the changes.

## Running

To run a solution by day, use:

```bash
yarn start day1
```

If a solution exists for that day, then it will run with basic tests. If a solution does not exist, it will copy the template, and then try to download that day's puzzle input using [AOCD](https://github.com/wimglenn/advent-of-code-data).

If you don't have AOCD configured, populate `input.txt` with your solution input from the AOC website, and then start implementing your solution in the new folder for that day.

Once you have calculated a solution, you should manually submit your answer through the website.

## Viewer

A local webserver has been provided to browse the solutions, and optionally create web based visualisations to go with the code.

To start the server run: `yarn webserver` - a new hardcoded index.html will be generated each time you browse the index.

If you enable github pages from your repo settings, and host from the root of the project, you'll be able to access this index and the solutions from the provided hosted URL. Please replace this message with a link to those pages if you do.
