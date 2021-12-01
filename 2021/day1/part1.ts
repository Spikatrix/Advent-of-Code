import fs from "fs";

const fileContent: string = fs.readFileSync('input', 'utf8');
const lines: string[] = fileContent.split("\n").filter(line => line.trim());
const values: number[] = lines.map(line => parseInt(line));

let index = 0;
let incCount = 0;
while (index < values.length - 1) {
	if (values[index + 1] > values[index]) {
		incCount++;
	}
	index++;
}

console.log(incCount);