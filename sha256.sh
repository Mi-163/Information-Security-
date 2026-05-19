#!/bin/bash
#this script generates a sha256 hash of a specified file and stores it in hash.txt. It then checks the integrity of the file by comparing the current hash with the stored hash.
read -p "enter file name: " file

sha256sum "$file" > hash.txt

echo "hash stored in hash.txt"

echo "checking integrity..."

sha256sum -c hash.txt 
