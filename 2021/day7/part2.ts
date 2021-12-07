import fs from "fs";

const fileContent: string = fs.readFileSync('input', 'utf8');
const lines: string[] = fileContent.split("\n").filter(line => line.trim());

const crabs: number[] = lines[0].split(",").map(crabStr => parseInt(crabStr));

// Too lazy to make this efficient

function calc(num: number): number {
	let val: number = 0;
	for (let i = 1; i <= num; i++) {
		val = val + i;
	}
	return val;
}

let lowestFuel: number = 999999999;
for (let pos = 0; pos < 9999; pos++) {
	let fuelUsed: number = 0;
	crabs.forEach(crab => {
		fuelUsed += calc(Math.abs(crab - pos));
	});
	if (fuelUsed < lowestFuel) {
		lowestFuel = fuelUsed;
	}
}

console.log(lowestFuel);
