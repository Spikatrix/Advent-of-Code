import fs from "fs";

const fileContent: string = fs.readFileSync('input', 'utf8');
const lines: string[] = fileContent.split("\n").filter(line => line.trim());

const crabs: number[] = lines[0].split(",").map(crabStr => parseInt(crabStr));

// Too lazy to make this efficient

let lowestFuel: number = 99999999;
crabs.forEach(target => {
	let fuelUsed: number = 0;
	crabs.forEach(crab => {
		fuelUsed += Math.abs(crab - target);
	});
	if (fuelUsed < lowestFuel) {
		lowestFuel = fuelUsed;
	}
});

console.log(lowestFuel);
