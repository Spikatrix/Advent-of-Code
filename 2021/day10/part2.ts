import fs from "fs";

const fileContent: string = fs.readFileSync('input', 'utf8');
const lines: string[] = fileContent.split("\n").filter(line => line.trim());

const stackList: Array<string[]> = [];
lines.forEach(line => {
	const stack: string[] = [];
	const isValidLine = line.split('').every(char => {
		if ('{[<('.indexOf(char) !== -1) {
			stack.push(char);
		} else if (stack.length > 0 && (
				stack[stack.length - 1] === '(' && char === ')' ||
				stack[stack.length - 1] === '[' && char === ']' ||
				stack[stack.length - 1] === '{' && char === '}' ||
				stack[stack.length - 1] === '<' && char === '>')) {
			stack.pop();
		} else {
			return false;
		}

		return true;
	});

	if (isValidLine) {
		stackList.push(stack);
	}
});

let points: number[] = [];
stackList.forEach(stack => {
	let score: number = 0;
	let char = stack.pop();
	while (char) {
		score *= 5;
		if (char === '(') score += 1;
		else if (char === '[') score += 2;
		else if (char === '{') score += 3;
		else if (char === '<') score += 4;

		char = stack.pop();
	}
	points.push(score);
});

points = points.sort((a, b) => (a > b) ? 1 : -1);
console.log(points[Math.floor(points.length / 2)])