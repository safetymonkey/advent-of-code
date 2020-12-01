const solutionId = process.argv[2];
import fs from "fs";

const runSolution = (day) =>
  require(`./solutions/${solutionId}/solution.ts`).run(day);

const copyCodeTemplate = async () => {
  try {
    await require("./copy-template.ts");
    await runSolution(solutionId);
  } catch (ex) {
    console.error(
      `Unable to run solution for '${solutionId}': ${ex}`,
      ex.stack
    );
  }
};

const start = async () => {
  try {
    if (fs.existsSync(`./solutions/${solutionId}/solution.ts`)) {
      await runSolution(solutionId);
    } else {
      await copyCodeTemplate();
    }
  } catch (ex) {
    if (!solutionId) {
      console.error(
        "No solution ID provided; please re-run with an argument, e.g.: npm start day1, or: node run day1"
      );
    } else {
      await copyCodeTemplate();
    }
  }
};

start();
