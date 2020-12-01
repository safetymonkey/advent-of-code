import path from "path";
import { read, write, position } from "promise-path";
const fromHere = position(__dirname);
export const reportGenerator = (filename: string) => async (
  ...messages: string[]
) =>
  console.log(
    `[${require(await fromHere("./package.json")).logName} / ${filename
      .split(path.sep)
      .pop()
      ?.split(".ts")
      .shift()}]`,
    ...messages
  );

export const replaceInFile = async (
  filename: string,
  search: string | RegExp,
  replace: string
): Promise<any> => {
  const haystack: string = await read(filename, "utf8");
  const ashes: string = haystack.replace(search, replace);
  return write(filename, ashes, "utf8");
};
