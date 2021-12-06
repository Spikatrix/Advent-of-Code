import fs from "fs";

const fileContent: string = fs.readFileSync('input', 'utf8');
const lines: string[] = fileContent.split("\n").filter(line => line.trim());

const timers: number[] = lines[0].split(",").map(timerStr => parseInt(timerStr));
const days = 80;

for (let day = 0; day < days; day++) {
	let newFishCount = 0;
	timers.forEach((timer, index) => {
		timers[index]--;
		if (timers[index] < 0) {
			timers[index] = 6;
			newFishCount++;
		}
	});
	while (newFishCount--) {
		timers.push(8);
	}
}

console.log(timers.length);