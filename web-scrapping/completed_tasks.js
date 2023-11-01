#!/usr/bin/node
// A script  that prints the number of movies where the character 
// “Wedge Antilles” is present.

const request = require('request');

const url = process.argv[2];

request(url, function (error, response) {
	if (error) {
		console.error('error:', error);
	}

	computed_obj = {};
	const result = JSON.parse(response.body);

	for (let user of result) {
		if (user.completed) {
			computed_obj[user.userId] = computed_obj[user.userId] >= 1 ? 
			computed_obj[user.userId] + 1:  1;
		}		
	}
	console.log(computed_obj);
});