import fs from "fs";

const fileContent: string = fs.readFileSync('input', 'utf8');
const lines: string[] = fileContent.split("\n").filter(line => line.trim());

type Player = { position: number, score: number }
const players: Player[] = [];
const rolls: number = 3;

lines.forEach(line => {
	players.push({
		position: parseInt(line.split(":")[1].trim()),
		score: 0,
	});
})

let dice: number = 1;
let diceRollCount: number = 0;
while (!players.find(player => player.score >= 1000)) {
	players.forEach((player, index) => {
		for (let i = 0; i < rolls; i++) {
			player.position = (player.position + dice) % 10;
			if (player.position === 0) {
				player.position = 10;
			}
			dice++;
			diceRollCount++;
			if (dice > 100) {
				dice = 1;
			}
		}
		player.score += player.position;
	})
};

const losingPlayer = players.find(player => player.score < 1000)!;
console.log((diceRollCount - ((players.length - 1) * rolls)) * (losingPlayer.score - losingPlayer.position));