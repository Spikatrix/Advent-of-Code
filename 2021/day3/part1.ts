import fs from "fs";

const fileContent: string = fs.readFileSync('input', 'utf8');
const lines: string[] = fileContent.split("\n").filter(line => line.trim());

let gamma = '', epsilon = '';

const lineLen = lines[0].length;
for (let i = 0; i < lineLen; i++) {
	let oneCount = 0, zeroCount = 0;
	lines.forEach(line => {
		if (line[i] === '1') {
			oneCount++;
		} else {
			zeroCount++;
		}
	});

	if (oneCount > zeroCount) {
		gamma += '1';
		epsilon += '0';
	} else {
		gamma += '0';
		epsilon += '1';
	}
}


console.log(parseInt(gamma, 2) * parseInt(epsilon, 2));