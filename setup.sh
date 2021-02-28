#!/bin/bash

# Run ./setup.sh [TOKEN]

var=""

echo "Please install the dependences before running this script"
printf "Are the dependences installed? [Y/n] "
read var

if test $var != "Y"
then
  echo "Exiting..."
  exit -1
fi

echo "TOKEN=$1" >> commands/Variables.py
python3 bot.py

exit 0
