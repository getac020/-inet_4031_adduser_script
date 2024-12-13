# INET4031 Add Users Script and User List

## Purpose 
The purpose of the Add Users Script is to automate the process of adding multiple users and groups to a Linux system. This script simplifies and accelerates the user management process, reducing the potential for human error and ensuring consistency in user account creation.

## What It Does 
The script reads user data from an input file and performs the following actions:

* User Creation: Adds new user accounts based on the provided data, including usernames, passwords, last names, and first names.

* Group Assignment: Assigns users to specified groups, ensuring proper permissions and access controls within the system.

* Automated Execution: Allows administrators to run the script using a single command, streamlining the user addition process.

## Program Operation
Follow the following steps to run the code. 
    1. make sure you have an input file with user data in the 
    following format
        username:password:last_name:first_name:groups
    2. Run the script using the following command
        sudo ./create-users.py < [input file name].input

After running the script check if the users are created correctly using
the following commands
    1. grep user0 /etc/passwd
    2. grep user0 /etc/group


# Steps taken for assignment

* Create a GitHub Repository for Storing Code:

** Created a new GitHub repository named inet_4031_adduser_script.

** Synchronized this repository to a local repository on an Ubuntu server.

** Pushed local repo changes to the remote GitHub repo for synchronization.

* Create the 'create-users.py' Script:

** Navigated to the new repository directory.

** Created the create-users.py file and added starter Python code to automate adding users and groups.

* Create the 'create-users.input' File:

** Created the create-users.input file containing user data.

** Input file contained a colon-delimited list of usernames, passwords, last names, first names, and groups.

* Create Users with the 'create-users.py' Script:

** Ran the create-users.py script to process the input file and create user accounts.

** Included mechanisms to skip specific users and handle incorrectly formatted lines.

* Confirm the Users Have Been Created:

** Verified user and group creation using command-line tools.

** Checked for successful execution of the script by inspecting system files.


