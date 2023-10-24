#!/usr/bin/node
// A script  that prints the number of movies where the character 
// “Wedge Antilles” is present.

const request = require('request')
const movie_url = process.argv[2]
let counter = 0

request(movie_url, function (error, response) {
	if (error) {
		console.error('error:', error); // Print the error if one occurred
	}
	const result_injson = JSON.parse(response.body)

	const data = result_injson.results

	for (let obj of data) {
		for (let character of obj.characters) {
			if (character === 'https://swapi-api.alx-tools.com/api/people/18/') {
				counter += 1;
			}
		}
	}
	console.log(counter); 
});