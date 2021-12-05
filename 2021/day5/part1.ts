import fs from "fs";

const fileContent: string = fs.readFileSync('input', 'utf8');
const lines: string[] = fileContent.split("\n").filter(line => line.trim());

// This whole code is ugly and inefficient

type Point = { x: number, y: number }
type Line = { src: Point, dest: Point };
const lineData: Line[] = [];

lines.forEach(line => {
	const [srcPoints, _, destPoints] = line.split(" ");
	let coords = srcPoints.split(",").map(pointStr => parseInt(pointStr));
	const srcPoint: Point = { x: coords[0], y: coords[1] };
	coords = destPoints.split(",").map(pointStr => parseInt(pointStr));
	const destPoint: Point = { x: coords[0], y: coords[1] };
	lineData.push({ src: srcPoint, dest: destPoint });
});

const gridLoc: Point[] = [];
let twoOrMoreCount: number = 0;

function addPoint(point: Point) {
	gridLoc.push({ ...point });
	if (gridLoc.filter(loc => loc.x === point.x && loc.y === point.y).length === 2) {
		twoOrMoreCount++;
	}
}

lineData.forEach(line => {
	let currentPoint = line.src;
	if (currentPoint.x !== line.dest.x && currentPoint.y !== line.dest.y) {
		return;
	}

	addPoint(currentPoint);
	while (currentPoint.x !== line.dest.x || currentPoint.y !== line.dest.y) {
		const xDiff = line.dest.x - currentPoint.x;
		const yDiff = line.dest.y - currentPoint.y;
		if (xDiff > 0) {
			currentPoint.x++;
		} else if (xDiff < 0) {
			currentPoint.x--;
		}

		if (yDiff > 0) {
			currentPoint.y++;
		} else if (yDiff < 0) {
			currentPoint.y--;
		}

		addPoint(currentPoint);
	}
});

console.log(twoOrMoreCount);