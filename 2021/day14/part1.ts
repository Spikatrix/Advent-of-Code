import fs from "fs";

const fileContent: string = fs.readFileSync('input', 'utf8');
const lines: string[] = fileContent.split("\n").filter(line => line.trim());

type Rule = { lhs: string, rhs: string };
let polymer: string = lines[0];
const rules: Rule[] = [];
const monomers: string[] = [];

lines.slice(1).forEach(ruleLine => {
	const [ lhs, rhs ] = ruleLine.split(' -> ');
	rules.push({ lhs, rhs });
});

polymer.split('').forEach(monomer => {
	if (!monomers.includes(monomer)) {
		monomers.push(monomer);
	}
});

rules.forEach(rule => {
	if (!monomers.includes(rule.rhs)) {
		monomers.push(rule.rhs);
	}
})

for (let step = 0; step < 10; step++) {
	let newPolymer = polymer;
	for (let i = polymer.length - 1; i >= 0; i--) {
		const rule = rules.find(rule => rule.lhs === polymer.slice(i, i + 2));
		if (!rule) {
			continue;
		}
		newPolymer = newPolymer.slice(0, i + 1) + rule.rhs + newPolymer.slice(i + 1);
	}
	polymer = newPolymer;
}

let most: number = 0, least: number = 999999999;
monomers.forEach(monomer => {
	const count = polymer.split('').filter(m => m === monomer).length;
	if (count > most) {
		most = count;
	}
	if (count < least) {
		least = count;
	}
})

console.log(most - least)