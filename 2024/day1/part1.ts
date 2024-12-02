import fs from "fs";

const fileContent: string = fs.readFileSync('input', 'utf8');
const lines: string[] = fileContent.split("\n").filter(line => line.trim());

let list1: number[] = []
let list2: number[] = []
lines.forEach(line => line.split(" ").filter(Boolean)
	.forEach((number, index) => (index === 0 ? list1 : list2).push(parseInt(number))))

list1 = list1.sort((a, b) => a - b)
list2 = list2.sort((a, b) => a - b)

let distance = 0
list1.forEach((number, index) => distance += Math.abs(number - list2[index]))

console.log(distance)