#this script checks if a user is logged in and keeps checking every 30 seconds until the user logs in.

#!/bin/bash

read -p "enter user name: " user

until who | grep -wq "$user"; do

  echo "user '$user' not logged in..trying again in 30 sec"
 
  sleep 30

done

echo "user '$user' logged  in"
