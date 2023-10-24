#!/usr/bin/node
// A script that reads and prints the content of a file.


const {readFileSync} = require('fs')
file_name = process.argv[2]
const content = readFileSync(file_name)

console.log(content.toString())
