import fs from "fs";

const fileContent: string = fs.readFileSync('input', 'utf8');
const lines: string[] = fileContent.split("\n").filter(line => line.trim());

let depth = 0, hPos = 0, aim = 0;
lines.forEach(line => {
	const [action, valueStr] = line.split(" ");
	const value = parseInt(valueStr);
	if (action === "forward") {
		hPos += value;
		depth += (aim * value);
	} else if (action === "down") {
		aim += value;
	} else if (action === "up") {
		aim -= value;
	}
});

console.log(depth * hPos);