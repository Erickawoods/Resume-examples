#!/bin/bash
# Lets create a while loop than runs a conditinal statment
#Ask the user for an input if they choose:
# 1 then echo hello world
# 2 ping a website or ip address
# 3 run ifconfig
# else echo invalid entry

user=y
while [ "$user = y" ]
do
echo "Choose an option between 1-3:"
echo "1. Hello World"
echo "2. Ping a website or ip address"
echo "3. Run ifconfig"
read input   
   
if [ $input = 1 ] 
    then echo "Hello World"

elif [ $input = 2 ]; 
    then echo "Enter IP address to ping"
    read -r address
    ping "$address"

elif [ "$input = 3" ]; 
then ifconfig

else 
    echo "Invalid Entry" 
fi

echo "Choose an option between 1-3:"
read user

done

echo "Good Work"

