#!/usr/bin/env python3
###########################
# Title: OpsChallenge11
# Author:Jeff Snyder
# Date: 19OCT2020
# Purpose: Scan ports
###########################
import smtplib
import random
import sys 
from scapy.all import *


def scanIP(targetIP,targetPort):
    port_range= []
    for x in port_range:
        if x <= targetPort
            host = targetIP
            src_port = random.randint(1,65535)
            dst_port =
    
        response = sr1(IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=1,verbose=0)
    print(response)

def main():
    print("Do you want to play a game?")
    targetIP=input("What is the ip address you would like to scan?")
    targetPort=input("What is the port range you would like to scan?(0-65,535)")
    scanIP(targetIP,targetPort)
main()