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

	rotate () {
		let temp = this.width;
		this.width = this.height;
		this.height = temp

		return this;
	}

	double () {
		
		this.width = this.width * 2;
		this.height = this.height * 2;

		return this;
	}
}

module.exports = Rectangle