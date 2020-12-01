import { run, position } from "promise-path";
import { reportGenerator, replaceInFile } from "./util";

const report = reportGenerator(__filename);

const fromHere = position(__dirname);
const setup = async (): Promise<void> => {
  const currentPath: string = fromHere("/");
  console.log(currentPath);
  const currentFolder: string = currentPath.split("/").reverse()[1];

  report("Setting up template from:", currentFolder);

  const currentYear: string | undefined = currentFolder.split("-").pop();

  if (currentYear === "template") {
    console.error("  No current year provided.");
    console.error(
      "  Please re-run setup after renaming the repo, e.g.: advent-of-code-2020, advent-of-code-2021, advent-of-code-2022, etc."
    );
    console.error("");
    process.exit(0);
  }

  report("Replacing strings in templates");
  await replaceInFile(
    "README.md",
    "If using the Advent of Code Template repo; click [**`Use this template`**](https://github.com/johnbeech/advent-of-code-nodejs-template/generate) and set a new repository name.\n",
    ""
  );
  await replaceInFile(
    "README.md",
    "If this a brand new repository, run: `node setup` to configure it for Current Year and check in the changes.\n",
    ""
  );

  await replaceInFile(
    "package.json",
    /Advent of Code Template/g,
    `Advent of Code ${currentYear}`
  );
  await replaceInFile(
    "README.md",
    "# Advent of Code Template",
    `# Advent of Code ${currentYear}`
  );

  await replaceInFile(
    "package.json",
    "Advent of Code Template using Node JS for Current Year.",
    `My solutions for Advent of Code ${currentYear}.`
  );
  await replaceInFile(
    "README.md",
    "Advent of Code Template using Node JS for Current Year.",
    `My solutions for Advent of Code ${currentYear}.`
  );

  await replaceInFile("package.json", "advent-of-code-template", currentFolder);

  report("Removing setup script");
  await run(`rm ${fromHere("setup.js")}`);

  report("Committing changes and pushing to remote");
  await run("git add .");
  await run(`git commit -m "Setup template for Current Year (${currentYear})"`);
  await run("git push");

  report(`All done! ${currentYear} setup and ready to go~`);
};

setup();
