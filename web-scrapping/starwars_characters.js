#!/usr/bin/node
// A script that prints all characters of a Star Wars movie 

const request = require('request')
const baseUrl = 'https://swapi-api.alx-tools.com/api/films/'
const url = baseUrl + `${process.argv[2]}`

let result = {}
request(url, function (error, response) {
	if (error) {
		console.error('error:', error); // Print the error if one occurred
	}
	result = JSON.parse(response.body)

	for (let character of result.characters) {
			request(character, function (error, response) {
				if (error) {
					console.error('error:', error);
				}
			
				computed_obj = {}
				result = JSON.parse(response.body)
			
				console.log(result.name)

			});
	}
	
});




