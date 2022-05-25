#!/bin/bash
# Read from the file words.txt and output the word frequency list to stdout.
tr -s ' ' '\n' < words.txt | sort | uniq -c | sort -r | awk '{print $2, $1}'

# Change spaces to new lines, sort the words and get the unique words.
# Count the number of occurences of each unique word and sort descending order.
# Print out the word then number of occurences
