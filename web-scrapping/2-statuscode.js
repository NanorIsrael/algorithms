#!/usr/bin/node
// A script that reads and prints the content of a file.


const request = require('request')
const url = process.argv[2]

request(url, function (error, response) {
	if (error) {
		console.error('error:', error); // Print the error if one occurred
	}
  	console.log('code:', response && response.statusCode); // Print the response status code if a response was received
  
});