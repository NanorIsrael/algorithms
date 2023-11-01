#!/usr/bin/node
// A script  that prints the number of movies where the character 
// “Wedge Antilles” is present.

const request = require('request');
const {writeFileSync} = require('fs');
const url = process.argv[2];
const file_name = process.argv[3];

request(url, function (error, response) {
	if (error) {
		console.error('error:', error);
	}
	const content = response.body;
	writeFileSync(file_name, content, 'utf-8');
});