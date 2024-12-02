import fs from "fs";

const fileContent: string = fs.readFileSync('input', 'utf8');
const lines: string[] = fileContent.split("\n").filter(line => line.trim());

let list1: number[] = []
let list2: number[] = []
lines.forEach(line => line.split(" ").filter(Boolean)
	.forEach((number, index) => (index === 0 ? list1 : list2).push(parseInt(number))))

let distance = 0
list1.forEach(number => distance += (number * list2.reduce((acc, curr) => acc += (number === curr ? 1 : 0), 0)))

console.log(distance)