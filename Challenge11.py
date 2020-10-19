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
        targetPort= int(targetPort)
        i = 1
        while i < targetPort:
            host = targetIP
            src_port = random.randint(1,65535)
            dst_port =i
            
            response = sr1(IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=5,verbose=0)
            if response is None:
                print("Packet filtered")
            elif(response.haslayer(TCP)):
                if(response.getlayer(TCP).flags ==0x12):
                    send_rst = sr(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="R"),timeout=5)
            elif(response.haslayer(TCP)):
                if(response.getlayer(TCP).flags ==0x14):
                    send_rst = sr(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="F"),timeout=5)
                    print("This port is closed")

            i +=1
            print(response, i)

def main():
    print("Do you want to play a game?")
    targetIP=input("What is the ip address you would like to scan?")
    targetPort= input("What is the port range you would like to scan?(0-65,535)")
    scanIP(targetIP,targetPort)
main()