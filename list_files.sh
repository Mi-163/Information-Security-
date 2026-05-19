#!/bin/bash

count=1

echo "S.No|File Name|Creation Date"
echo "--------------------------------"

for file in *; do
  if [ ! -f "$file" ]; then
     continue
  fi

  date=$(stat -c %w "$file" 2>/dev/null)
 
  if [ "$date"="-" ] || [ -z "$date" ]; then
    date=$(stat -c %y "$file" | cut -d' ' -f1)
  fi

 echo "$count|$file|$date"
 count=$((count+1))
done
