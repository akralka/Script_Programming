import { Operation } from './module.js';

const x = parseInt(process.argv[2]); // pobranie pierwszego argumentu z linii komend
const y = parseInt(process.argv[3]); // pobranie drugiego argumentu z linii komend

const op = new Operation(x, y);
console.log(`Sum is ${op.sum()}`);

// node index.js 2 9