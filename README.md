#INET4031 Add Users Script and User List

##Program Description
This Python script automates the addition of multiple users and groups to a Linux system by reading data from an input file. 
##Program Operation
Follow the folling steps to run the code. 

1. make sure you have a an input file with user data in the following format
    username:password:last_name:first_name:groups
2. Run the script using the following command
    sudo ./create-users.py < [input file name].input
