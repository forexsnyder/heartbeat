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
from shutil import copyfile
from sys import exit
from scapy.all import *
import ipaddress


def sniffNetwork():
    ipAddress='192.168.29.141'
    #sniff


def cracker(user, ipAddress, badFile, secret ):
    source = "C:\User\iexplorer\Downloads\registration.exe"
    target = "C:\User\iexplorer\Downloads\registration.exe"
    s=pxssh.pxssh()
    try:
        copyfile(source, target)
    
    try:
        s.login(ipAddress, user, secret)
        s.sendline("cd C:\User\iexplorer\Downloads\registration.exe")
        break    
    except pxssh.ExceptionPxssh as e:
        print ("pxssh failed to login")
        print(e)
        time.sleep(1)



def main():
    # encrypt()
    # sniffNetwork()
    # bruteforce () return password
    # transferfiles
    # 

main()

