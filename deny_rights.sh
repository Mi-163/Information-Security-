#!/bin/bash
#this script denies execution rights to a specified file.order of running commands(in terminal):
#1. chmod +x deny_rights.sh
#2. chmod +x sample.sh (or any file you want to deny execution)
#3. ./deny_rights.sh
#4. enter the file name(sample.sh) when prompted.
#5. ./sample.sh (you will get permission denied error)  
read -p "Enter file to be denied execution: " file

if [ -f "$file" ]; then
  chmod a-x "$file"
  echo "file execution denied"

else
  echo "file not found"

fi
