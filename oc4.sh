#!/bin/bash

# Lets create a function in bash that adds two number together
# Stretch goal can you do subtraction, multipliaction or division
# You will need to declare two variables

a=9
b=9

sum=$(( "$a + $b" ))

echo "Sum is: $sum"

sum=$(( "$a - $b" ))

echo "sum is: $sum"

sum=$(( "$a / $b" ))

echo "sum is: $sum"

sum=$(( "$a * $b" ))

echo "sum is: $sum"
