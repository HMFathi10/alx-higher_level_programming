#!/usr/bin/node
module.exports = class Square extends require ('./4-rectangle.js') {
	constructor (size) {
		super(size, size);
	}

	charPrint (c = 'X') {
		for (let i in range(this.size)
			console.log(c.repeat(this.size));
	}
};
