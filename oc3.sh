#!/bin/bash
# Condtinal Statment 
# This ops challenges is about conditinal stamtment of if else statments and how they work
# We are going to take a varibale with the number and have the computer tell us if its greater than 5 less than 5 or equals 5

x=0

if [ "$x" -eq "5" ]

then

echo "The number is 5"

elif [ "$x" -gt "5" ]

then

echo "The number is greater than 5"

else [ "$x" -lt "5" ]

echo "The number is less than 5"
fi
