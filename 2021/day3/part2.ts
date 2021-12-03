import fs from "fs";

const fileContent: string = fs.readFileSync('input', 'utf8');
const lines: string[] = fileContent.split("\n").filter(line => line.trim());

function hasMoreBit1(data: string[], index: number): boolean {
	let oneCount = 0, zeroCount = 0;
	data.forEach(line => {
		if (line[index] === '1') {
			oneCount++;
		} else {
			zeroCount++;
		}
	});

	return (oneCount >= zeroCount);
}

function getIntData(data: string[], replaceBit1: string, replaceBit2: string): number {
	let validData = [ ...data ];
	let currentIndex = 0;

	while (validData.length > 1) {
		const comp = hasMoreBit1(validData, currentIndex)
		validData = validData.filter(line => line[currentIndex] === (comp ? replaceBit1 : replaceBit2));
		currentIndex++;
	}

	return parseInt(validData[0], 2);
}

const o2: number = getIntData(lines, '1', '0');
const co2: number = getIntData(lines, '0', '1');

console.log(o2 * co2)