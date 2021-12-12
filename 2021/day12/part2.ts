import fs from "fs";

const fileContent: string = fs.readFileSync('input', 'utf8');
const lines: string[] = fileContent.split("\n").filter(line => line.trim());

const adjacencyMatrix: number[][] = []
const vertices: string[] = [];
lines.forEach(line => {
	const [src, dest] = line.split('-');
	if (!vertices.includes(src)) {
		vertices.push(src);
	}
	if (!vertices.includes(dest)) {
		vertices.push(dest);
	}
});

function printAdjacencyMatrix(matrix: number[][], vertices: string[]) {
	const axis = vertices.map(vertex => vertex.charAt(0))
	console.log('   ', axis.join('  '));
	matrix.forEach((row, index) => {
		console.log(axis[index], row)
	})
}

vertices.forEach(() => adjacencyMatrix.push(new Array(vertices.length).fill(0) as number[]));

lines.forEach(line => {
	const [srcIndex, destIndex] = line.split('-').map(vertex => vertices.indexOf(vertex));
	adjacencyMatrix[srcIndex][destIndex]++;
	adjacencyMatrix[destIndex][srcIndex]++;
});

let pathCount: number = 0;

function traverse(currentIndex: number, visitedVertices: string[] = [], visitedSmallTwice: boolean = false, fullPath: string[] = []) {
	const vertex = vertices[currentIndex];
	if (/^[a-z]*$/.test(vertex)) {
		visitedVertices.push(vertex);
	}
	fullPath.push(vertex);
	if (vertex === 'end') {
		pathCount++;
		return;
	}

	adjacencyMatrix[currentIndex].forEach((cell, cellIndex) => {
		if (cell && vertices[cellIndex] !== 'start') {
			const vertexIsVisited = visitedVertices.includes(vertices[cellIndex]);
			if (vertexIsVisited) {
				if (visitedSmallTwice) {
					return;
				}
				visitedSmallTwice = true;
			}

			traverse(cellIndex, [ ...visitedVertices ], visitedSmallTwice, [ ...fullPath ]);

			if (vertexIsVisited) {
				visitedSmallTwice = false;
			}
		}
		
	});
}

// printAdjacencyMatrix(adjacencyMatrix, vertices);

traverse(vertices.indexOf('start'));
console.log(pathCount);

