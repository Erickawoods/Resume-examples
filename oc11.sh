#!/bin/bash
# Given three integers (, , and ) representing the three sides of a triangle, identify whether the triangle is scalene, isosceles, or equilateral.
# If all three sides are equal, output EQUILATERAL.
# Otherwise, if any two sides are equal, output ISOSCELES.
# Otherwise, output SCALENE.
# Input Format
# Three integers, each on a new line.
# Constraints
# The sum of any two sides will be greater than the third.
# Output Format
# One word: either "SCALENE" or "EQUILATERAL" or "ISOSCELES" (quotation marks excluded).

# Read three integers as input
echo "Enter the length of side 1:"
read side1

echo "Enter the length of side 2:"
read side2

echo "Enter the length of side 3:"
read side3

# Check the type of triangle
if [ "$side1" -eq "$side2" ] && [ "$side2" -eq "$side3" ]; then
  echo "EQUILATERAL"
elif [ "$side1" -eq "$side2" ] || [ "$side1" -eq "$side3" ] || [ "$side2" -eq "$side3" ]; then
  echo "ISOSCELES"
else
  echo "SCALENE"
fi
