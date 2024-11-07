#!/usr/bin/python3

#### Student Name: Dagim Getachew
#### Program Name: Adduser script
#### Program creation Date: 11/6/2024
#### Program Last Updated Date: 11/6/2024


import os  # Aallows python to run os commands 
import re  # provides regular expression operations 
import sys # provides access to system-specific parameters and functions 

def main():

    #loops through each line provided by the input file
    for line in sys.stdin:

        #checks if the line is a comment(starts with #)
        match = re.match("^#",line)

        #splits the line into fields based on the colon separator
        fields = line.strip().split(':') 


        #skips processing for lines that are comments or are not formated properly 
        if match or len(fields) != 5:
            continue
            
        #extracting user information from the fields 
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])
        groups = fields[4].split(',')

        #creating user account with the provided GECOS field
        print("==> Creating account for %s..." % (username))
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        #executes commands in the systems shell
        os.system(cmd)

        #setting user's password
        print("==> Setting the password for %s..." % (username))
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        #executes commands in the systems shell
        os.system(cmd)

        #assigns the user to a specified groups
        for group in groups:
            #skip the dash, which indicates no group assignment
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                
                #executes commands in the systems shell
                os.system(cmd)

if __name__ == '__main__':
    main()
