import fs from "fs";

const fileContent: string = fs.readFileSync('input', 'utf8');
const lines: string[] = fileContent.split("\n").filter(line => line.trim());

const octopusEnergy: number[][] = lines.map(line => line.split('').map(char => parseInt(char)));
const tempGrid: number[][] = [];

type Coord = { x: number, y: number };

function flash(grid: number[][], coord: Coord): Coord[] {
	const reFlashCoords = [];

	const { y: rowIndex, x: colIndex } = coord;
	for(let i = -1; i <= 1; i++) {
		for (let j = -1; j <= 1; j++) {
			if (rowIndex + i < 0 || rowIndex + i >= grid.length ||
					colIndex + j < 0 || colIndex + j >= grid[0].length || 
					(i === 0 && j === 0) || grid[rowIndex + i][colIndex + j] < 0) {
				continue;
			}
			grid[rowIndex + i][colIndex + j]++;

			if (grid[rowIndex + i][colIndex + j] > 9) {
				reFlashCoords.push({ x: colIndex + j, y: rowIndex + i })
			}
		}
	}

	tempGrid[rowIndex][colIndex] = -1;
	return reFlashCoords;
}

let flashCount: number = 0;
for (let step = 1; step <= 100; step++) {
	// Populate tempGrid with original array elements
	tempGrid.length = 0;
	octopusEnergy.forEach(row => tempGrid.push([ ...row ]));

	let flashCoords: Coord[] = [];
	tempGrid.forEach((row, rowIndex) => row.forEach((_, colIndex) => {
		tempGrid[rowIndex][colIndex]++;
		if (tempGrid[rowIndex][colIndex] > 9) {
			flashCoords.push({ x: colIndex, y: rowIndex });
		}
	}));

	while (flashCoords.length > 0) {
		const flashCoord: Coord | undefined = flashCoords.pop();
		if (flashCoord) {
			const newCoords = flash(tempGrid, flashCoord);
			newCoords.forEach(coord => {
				if (!flashCoords.find(c => c.x === coord.x && c.y === coord.y)) {
					flashCoords.push(coord);
				}
			})
		}
	}

	// Copy tempGrid back to original array
	octopusEnergy.length = 0;
	tempGrid.forEach(row => octopusEnergy.push(row.map(cell => {
		if (cell === -1) {
			flashCount++;
			return 0;
		}
		return cell;
	})));
}

console.log(flashCount)
