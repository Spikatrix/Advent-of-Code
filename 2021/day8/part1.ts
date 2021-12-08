import fs from "fs";

const fileContent: string = fs.readFileSync('input', 'utf8');
const lines: string[] = fileContent.split("\n").filter(line => line.trim());

const countValues: number[] = [2, 4, 3, 7];
let count: number = 0;
lines.forEach(line => {
	const [ signalPatterns, outputValues ] = line.split("|");
	outputValues.split(" ").forEach(val => {
		if (countValues.includes(val.trim().length)) {
			count++;
		}
	});
});

console.log(count)