import fs from "fs";

const fileContent: string = fs.readFileSync('input', 'utf8');
const lines: string[] = fileContent.split("\n").filter(line => line.trim());

type Direction = 'x' | 'y'
type Point = { x: number, y: number };
type Fold = { direction: Direction, location: number };
let dots: Point[] = [];
const folds: Fold[] = [];

lines.forEach(line => {
	if (line.includes(',')) {
		const [ x, y ] = line.split(',').map(coordStr => parseInt(coordStr));
		dots.push({ x, y });
	} else if (line.includes('=')) {
		const [ directionStr, locationStr ] = line.substring(11).split('=');
		const direction = directionStr as Direction;
		const location = parseInt(locationStr);
		folds.push({ direction, location })
	}
});

folds.forEach(fold => {
	dots = dots.filter(dot => dot[fold.direction] !== fold.location);
	while (true) {
		const dotIndex = dots.findIndex(dot => dot[fold.direction] > fold.location);
		if (dotIndex === -1) {
			break;
		}


		const newDot = { ...dots[dotIndex] };
		dots.splice(dotIndex, 1);
		newDot[fold.direction] = 2 * fold.location - newDot[fold.direction];
		if (!dots.find(dot => dot.x === newDot.x && dot.y === newDot.y)) {
			dots.push(newDot);
		}
	}
});

for (var i = 0; i < 6; i++) {
	let rowStr: string = "";
	for (var j = 0; j < 39; j++) {
		if (dots.find(dot => dot.x === j && dot.y === i)) {
			rowStr += '#';
		} else {
			rowStr += ' ';
		}
	}
	console.log(rowStr);
}