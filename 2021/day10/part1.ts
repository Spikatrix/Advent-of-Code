import fs from "fs";

const fileContent: string = fs.readFileSync('input', 'utf8');
const lines: string[] = fileContent.split("\n").filter(line => line.trim());

let totalPoints: number = 0;
lines.forEach(line => {
	const stack: string[] = [];
	line.split('').every(char => {
		if ('{[<('.indexOf(char) !== -1) {
			stack.push(char);
		} else if (stack.length > 0 && (
				stack[stack.length - 1] === '(' && char === ')' ||
				stack[stack.length - 1] === '[' && char === ']' ||
				stack[stack.length - 1] === '{' && char === '}' ||
				stack[stack.length - 1] === '<' && char === '>')) {
			stack.pop();
		} else {
			if (char === ')') totalPoints += 3;
			else if (char === ']') totalPoints += 57;
			else if (char === '}') totalPoints += 1197;
			else if (char === '>') totalPoints += 25137;
			return false;
		}

		return true;
	});
});

console.log(totalPoints)