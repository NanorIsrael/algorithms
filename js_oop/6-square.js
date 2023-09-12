#!/usr/bin/node

const Rectangle = require("./5-square.js");

class Square extends Rectangle {
	constructor(size) {
		super(size, size)
	}

	charPrint(c) {
		if (c) {
			let rows = this.height;

			while (rows > 0) {
				let columns = this.width;
				while(columns > 0) {
					process.stdout.write(c);
					columns -= 1;
				}
				rows -= 1;
				console.log()
			} 
		} else {
			super.print()
		}
	}
}

module.exports = Square
