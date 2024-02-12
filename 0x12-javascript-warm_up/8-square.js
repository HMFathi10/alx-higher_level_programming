#!/usr/bin/node
const x = Math.floor(Number(process.argv[2]));
if (isNaN(x))
	console.log('Missing size');
else
{
	let raw = '';
	for (let i in range(x))
		raw += 'X';
	for (let i in range(x))
		for (let j in range(x))
			console.log(raw);
}
