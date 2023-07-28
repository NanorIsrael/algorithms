#!/usr/bin/env bash
#This script displays Best School 10 times using a while loop.

#!/bin/bash

file_path="school"

# Check if the file exists
if [ -e "$file_path" ]; then
    echo "school file exists"

    # Check if the file is empty
    if [ -s "$file_path" ]; then
        echo "school file is not empty"
    else
        echo "school file is empty"
    fi

    # Check if the file is a regular file
    if [ -f "$file_path" ]; then
        echo "school is a regular file"
    fi   
else
    echo "school file does not exist"
fi


i=1
while [ $i -ne 101 ]
do
  if [ "$i % 3" = "0" -a $(expr $i % 5) -eq 0 ]
  then
      echo "FizzBuzz"
  elif  (("$i % 3" == "0"));
  then
      echo "Fizz"
  elif (($i % 5 == 0));
  then
      echo "Buzz"
  else
      echo "$i"
  fi
  ((i = i + 1))
done

file_path="/etc/passwd"

if [ -e "$file_path" ]
then
  while IFS=: read -r username _ user_id _ _ home_dir _
  do
    echo "$username:$user_id:$home_dir"
  done < $file_path
fi


 while IFS=: read -r f1 f2 f3 f4 f5 f6 f7
  do
    echo "The user $f1 is part of the $f4 gang,
     lives in $f6 and rides $f7. $f3's 
     place is protected by the passcode $f2, 
     more info about the user here: $f5"

  done < $file_path

file_path="apache-access.log"
 while IFS=: read -r line
  do
    awk '/.*.*./ {print $1,$9}' $file_path

file_path="apache-access.log"
awk '{
    # Extract the IP and HTTP status code from each log line
    ip = $1
    http_code = $9

    # Group visitors by IP and HTTP status code and count the occurrences
    count[ip, http_code]++
}

# At the end, print the grouped data in the specified format
END {
    for (key in count) {
        split(key, keys, SUBSEP)
        printf "%d %s %s\n", count[key], keys[1], keys[2]
    }
}' $file_path | sort -nr

  # done < $file_path