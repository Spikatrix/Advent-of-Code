import fs from "fs";

const fileContent: string = fs.readFileSync('input', 'utf8');
const lines: string[] = fileContent.split("\n").filter(line => line.trim());

const inputs: number[] = lines[0].split(",").map(inputStr => parseInt(inputStr));
const boardSize = 5;

type BoardType = Array<number[]>;
const boards: BoardType[] = [];

// Get all board inputs
let lineIndex: number = 1;
while (lineIndex < lines.length) {
	const currentBoardIndex = boards.length;
	boards.push([]);
	let boardLineIndex = 0;
	while (boardLineIndex < boardSize) {
		const boardLineInts: number[] = lines[lineIndex].split(" ")
											.filter(value => value.trim())
											.map(valueStr => parseInt(valueStr));
		boards[currentBoardIndex].push(boardLineInts);
		boardLineIndex++;
		lineIndex++;
	}
}

let currentInputIndex: number = 4;
let wonBoard: number = -1;
while (wonBoard === -1) {
	const currrentInputs = inputs.slice(0, currentInputIndex);

	boards.some((board, boardIndex) => {
		const transpose: BoardType = board[0].map((_, colIndex) => board.map(row => row[colIndex]));

		const checkRow = (row: number[]) => row.every(value => currrentInputs.includes(value));
		if (board.some(checkRow) || transpose.some(checkRow)) {
			wonBoard = boardIndex;
		}

		return wonBoard !== -1;
	});

	currentInputIndex++;
}

const finalInputs = inputs.slice(0, currentInputIndex - 1);
let unmarkedSum = 0;
boards[wonBoard].forEach(row => {
	row.forEach(value => {
		if (!finalInputs.includes(value)) {
			unmarkedSum += value;
		}
	});
});

console.log(unmarkedSum * finalInputs[finalInputs.length - 1]);