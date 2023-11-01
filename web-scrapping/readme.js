#!/usr/bin/node
// A script that reads and prints the content of a file.

const {readFileSync} = require('fs')
file_name = process.argv[2]
readFileSync(file_name, (error, content) => {
        if (error) {
                console.log(error)
        }
        console.log(content.toString())
})
~                                                                                                
~                             