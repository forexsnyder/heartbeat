#!/usr/bin/env python3
###########################
# Title: OpsChallenge11
# Author:Jeff Snyder
# Date: 19OCT2020
# Purpose: Scan ports
###########################
import smtplib
import random
import itertools
import sys
import time
def mode1():
    filepath =input("What is the file path of the text file?   ")
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            print("{}".format(line.strip()))
            line = fp.readline()
            time.sleep(1)
            cnt += 1
def mode2():
    passwordCheck=input("Please enter the password to check.   ")
    filepath =input("What is the file path of the text file?   ")
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            line=line.strip()
            if line == passwordCheck:
                print("Your password of {} is a match in the dictionary".format(passwordCheck))
                break
            else:
                print("{}".format(line.strip()))
                line = fp.readline()
                time.sleep(1)
                cnt += 1



def main():
    print("Do you want to play a game?")
    print("Please select a mode. 1 for password cracking.  2 for checking a password against a dictionary")
    mode=input("Press 1 or 2.   ")
    if mode =="1":
            print("You have selected mode 1.")
            mode1()
    else:
            print("You have selected mode 2.")
            mode2()
main()



# with help from https://stackabuse.com/read-a-file-line-by-line-in-python/