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
from scapy.all import ICMP, IP, sr1, TCP


def scanIP(targetIP):
    host = targetIP
    port_range= 22
    src_port = 22
    dst_port =22
    
    response = sr1(IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=1,verbose=0)
    print(response)
def main():
    print("Do you want to play a game?")
    targetIP=input("What is the ip address you would like to scan?")
    scanIP(targetIP)
main()