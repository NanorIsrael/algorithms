#!/usr/bin/node

class Rectangle {
	constructor(w, h) {
		if (w > 0 && h > 0) {
			this.width = w;
			this.height = h
		}
	}

	print () {
		let rows = this.height;

		while (rows > 0) {
			let columns = this.width;
			while(columns > 0) {
				process.stdout.write('X');
				columns -= 1;
			}
			rows -= 1;
			console.log()
		} 
	}
}

module.exports = Rectangle
