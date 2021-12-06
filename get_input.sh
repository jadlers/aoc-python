#!/bin/sh

# To get input for day 3 the current year:
# ./get_input.sh 3

if [ ! -f "./cookie.txt" ]; then
  echo "A 'cookie.txt' file is required to fetch data"
  echo "It should export a header for the session to be used by curl"
  echo "  Example cookie='cookie: session=<your session>'"
  exit 1
fi

year="$2"
if [ -z "$year" ]; then
  year=$(date +%Y)
fi

if [ "$#" -lt 1 ]; then
  echo "Usage: $0 <day> [year]"
  exit 1
fi

day=$1

# Put your own session cookie in cookie.txt
# cookie='cookie: session=1234abcd..'
source ./cookie.txt

if [ -f "$year/$day.in" ]; then
  echo "You already have the input for day $day $year"
  exit 1
fi

curl "https://adventofcode.com/$year/day/${day}/input" -H "$cookie" --compressed \
  --output "$year/$day.in"
head "$year/$day"

