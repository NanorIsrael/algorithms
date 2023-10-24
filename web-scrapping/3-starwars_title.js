#!/usr/bin/node
// A script that  prints the title of a Star Wars movie 
// where the episode number matches a given integer.

const request = require('request')
const movie_id = process.argv[2]
const url = `https://swapi-api.alx-tools.com/api/films/${movie_id}`

request(url, function (error, response) {
	if (error) {
		console.error('error:', error); // Print the error if one occurred
	}
	const result_injson = JSON.parse(response.body)
  	console.log(result_injson.title); // Print the response status code if a response was received
  
});