#!/usr/bin/env python3
###########################
# Title: OpsChallenge16
# Author:Jeff Snyder
# Date: 26OCT2020
# Purpose: Check or Guess passwords against a dictionary
###########################
import smtplib
import itertools
import sys
import time


def mode1():
    filepath =input("What is the file path of the text file?   ")
    with open(filepath) as fp:
        line = fp.readline()
        while line:
            print("{}".format(line.strip()))
            line = fp.readline()
            # print(line)
            time.sleep(1)
def mode2():
    passwordCheck=input("Please enter the password to check.   ")
    filepath =input("What is the file path of the text file?   ")
    with open(filepath) as fp:
        line = fp.readline()
        while line:
            line=line.strip()
            if line == passwordCheck:
                print("Your password of {} is a match in the dictionary".format(passwordCheck))
                break
            else:
                print("{}".format(line.strip()))
                line = fp.readline()




def main():
    print("Shall we play a game?")
    print("Please select a mode. 1 for password cracking.  2 for checking a password against a dictionary.")
    mode=input("Press 1 or 2.   ")
    if mode =="1":
            print("You have selected mode 1.")
            mode1()
    elif mode =="2":
            print("You have selected mode 2.")
            mode2()
    else:
        print("Attention to detail.")
        print("Attention to detail.")
        print("Attention to detail.")
        print("Attention to detail.")
        print("Attention to detail.")
        print("Attention to detail.")
        print("Attention to detail.")
        print("Attention to detail.")
        main()
main()



# with help from https://stackabuse.com/read-a-file-line-by-line-in-python/