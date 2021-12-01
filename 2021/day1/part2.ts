import fs from "fs";

const fileContent: string = fs.readFileSync('input', 'utf8');
const lines: string[] = fileContent.split("\n").filter(line => line.trim());
const values: number[] = lines.map(line => parseInt(line));

let windowSum: number[] = [];
const windowSize = 3;
let index = 0;
while (index < values.length - windowSize + 1) {
	windowSum.push(values.slice(index, index + windowSize).reduce((p, c) => p + c, 0));
	index++;
}

index = 0;
let incCount = 0;
while (index < windowSum.length - 1) {
	if (windowSum[index + 1] > windowSum[index]) {
		incCount++;
	}
	index++;
}

console.log(incCount);