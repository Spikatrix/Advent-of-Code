import fs from "fs";

const fileContent: string = fs.readFileSync('input', 'utf8');
const lines: string[] = fileContent.split("\n").filter(line => line.trim());

const heightMap: Array<number[]> = [];

lines.forEach(line => heightMap.push(line.split('').map(char => parseInt(char))));

let riskSum: number = 0;
heightMap.forEach((heightMapRow, row) => {
	heightMapRow.forEach((cell, col) => {
		if (!((col > 0 && heightMapRow[col - 1] <= cell) ||
			(col < heightMapRow.length - 1 && heightMapRow[col + 1] <= cell) ||
			(row > 0 && heightMap[row - 1][col] <= cell) ||
			(row < heightMap.length - 1 && heightMap[row + 1][col] <= cell))) {
				riskSum += (1 + cell);
			}
	});
});

console.log(riskSum)