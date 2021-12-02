import fs from "fs";

const fileContent: string = fs.readFileSync('input', 'utf8');
const lines: string[] = fileContent.split("\n").filter(line => line.trim());

let depth = 0, hPos = 0;
lines.forEach(line => {
	const [action, valueStr] = line.split(" ");
	const value = parseInt(valueStr);
	if (action === "forward") {
		hPos += value;
	} else if (action === "down") {
		depth += value;
	} else if (action === "up") {
		depth -= value;
	}
});

console.log(depth * hPos);