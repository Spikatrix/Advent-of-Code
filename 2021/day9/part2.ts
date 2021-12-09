import fs from "fs";

const fileContent: string = fs.readFileSync('input', 'utf8');
const lines: string[] = fileContent.split("\n").filter(line => line.trim());

const heightMap: Array<number[]> = [];

lines.forEach(line => heightMap.push(line.split('').map(char => parseInt(char))));

type Point = { x: number, y: number };
let lowPoints: Point[] = [];
heightMap.forEach((heightMapRow, row) => {
	heightMapRow.forEach((cell, col) => {
		if (!((col > 0 && heightMapRow[col - 1] <= cell) ||
			(col < heightMapRow.length - 1 && heightMapRow[col + 1] <= cell) ||
			(row > 0 && heightMap[row - 1][col] <= cell) ||
			(row < heightMap.length - 1 && heightMap[row + 1][col] <= cell))) {
				lowPoints.push({ x: col, y: row });
			}
	});
});

const basinSizes: number[] = [];
const checkedPoints: Point[] = [];
let checkIndex = 0;

function findAdjacentPoints(currentPoint: Point): number {
	const { x, y } = currentPoint;
	const cell = heightMap[y][x];
	const ptLen = checkedPoints.length;

	if (cell + 1 === 9) {
		return 0;
	}

	if (x > 0 && heightMap[y][x - 1] > cell && heightMap[y][x - 1] !== 9 &&
			checkedPoints.findIndex(pt => pt.x === x - 1 && pt.y == y) === -1) {
		checkedPoints.push({ x: x - 1, y });
	}
	if (x < heightMap[y].length - 1 && heightMap[y][x + 1] > cell && heightMap[y][x + 1] !== 9 && 
			checkedPoints.findIndex(pt => pt.x === x + 1 && pt.y == y) === -1) {
		checkedPoints.push({ x: x + 1, y });
	}
	if (y > 0 && heightMap[y - 1][x] > cell && heightMap[y - 1][x] !== 9 && 
			checkedPoints.findIndex(pt => pt.x === x && pt.y == y - 1) === -1) {
		checkedPoints.push({ x, y: y - 1 });
	}
	if (y < heightMap.length - 1 && heightMap[y + 1][x] > cell && heightMap[y + 1][x] !== 9 &&
			checkedPoints.findIndex(pt => pt.x === x && pt.y == y + 1) === -1) {
		checkedPoints.push({ x, y: y + 1 });
	}

	return checkedPoints.length - ptLen;
}


lowPoints.forEach(point => {
	let size = 1;
	checkedPoints.push(point);
	while (checkIndex < checkedPoints.length) {
		size += findAdjacentPoints(checkedPoints[checkIndex++]);
	}
	basinSizes.push(size);
});

let multi: number = 1;
for (let i = 0; i < 3; i++) {
	const max: number = basinSizes.reduce((pv, cv) => cv > pv ? cv : pv);
	basinSizes.splice(basinSizes.indexOf(max), 1);
	multi *= max;
}

console.log(multi);