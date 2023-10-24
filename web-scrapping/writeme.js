#!/usr/bin/node
// A script that reads and prints the content of a file.


const {writeFileSync} = require('fs')
const file_name = process.argv[2]
const content = process.argv[3]
writeFileSync(file_name, content, 'utf-8')

console.log(content.toString())
