#!/usr/bin/env python3
import paramiko, sys, os, socket

global host, username, line, input_file
line= "\n-----------------------------------------------------------------\n"

try:
    host="192.168.29.150"
    username="jeff"
    input_file= "/home/jeff/Desktop/sample.txt"

    if os.path.exists(input_file) == False:
        print("Path does not exist!")
def ssh_connect(password):
    ssh=paramiko.SSHClient()
    ssh.set_
