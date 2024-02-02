#!/bin/bash
# Bob is back at it again! Now he needs us to script something that if user inserts between 2 to 5, it will print out “Valid Number” and “your number is ___”.
# And if the user input is not between 2 and 5, it will print out “not valid!”
# Think about it and we will work on this together in class today! (edited) 

echo "Enter a number between 2 & 5"
read -r input

if [ $input -eq 2 ]; then
    echo "Your valid number is 2"
   
elif [ $input -eq 3 ]; then
    echo "Your valid number is 3"

elif [ $input -eq 4 ]; then
    echo "Your valid number is 4"
    
elif [ $input -eq 5 ]; then
    echo "Your valid number is 5"

else
    echo "Not a valid number!"
fi

