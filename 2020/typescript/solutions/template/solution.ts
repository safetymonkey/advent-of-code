import { read, position } from "promise-path";
import { reportGenerator } from "../../util";

const report = reportGenerator(__filename);
const fromHere = position(__dirname);

export async function run(day: string) {
  const input = (
    await read(fromHere(`solutions/${day}` + "/input.txt"), "utf8")
  ).trim();

  await solveForFirstStar(input);
  await solveForSecondStar(input);
}

async function solveForFirstStar(input) {
  const solution = "UNSOLVED";
  report("Input:", input);
  report("Solution 1:", solution);
}

async function solveForSecondStar(input) {
  const solution = "UNSOLVED";
  report("Solution 2:", solution);
}
