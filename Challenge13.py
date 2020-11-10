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
import ipaddress


def scanIP(targetIP,startPort,endPort):
        endPort= int(endPort)
        startPort= int(startPort)
        i = startPort
        while i <= endPort:
            host = targetIP
            src_port = random.randint(1,65535)
            dst_port =i
            
            response = sr1(IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=5,verbose=0)
            if response is None:
                send_rst = sr(IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="R"),timeout=5)
                print("Packet filtered")
            elif(response.haslayer(TCP)):
                if(response.getlayer(TCP).flags ==0x12):
                    send_rst = sr(IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="R"),timeout=5)
            elif(response.haslayer(TCP)):
                if(response.getlayer(TCP).flags ==0x14):
                    print("This port is closed")
            i +=1
            print(response, i)


def buildIPArray(cidrBlock):
    net= ipaddress.ip_network(cidrBlock)
    # skip first and last in the array
    ipaddressArray=[]
    ipaddressAvailable=[]
    ipaddressUnavailable=[]
    for a in net:
        ipaddressArray.append(a)
        # icmp = IP(dst=a)/ICMP()
        # resp = sr1(icmp,timeout=10)
        # print(resp)
    ipaddressArray= ipaddressArray[1:-1]
    for a in ipaddressArray:
        response=(
            sr1(IP(dst=a)/ICMP),
            timeout=5
        )
        if (response ==0):
            #print response
            #append to array of not available
        if (response ==1):
            #print response
            #append to array of available

    print(ipaddressArray)

    #replace print with skipping first and last in array.  Loop through array
        

def main():
    print("Shall we play a game?")
    mode=input("Select a mode. Enter 1 to scan an ip address. Enter 2 to ping a range of ip addresses.   ")

    if mode== "1":
        targetIP=input("What is the ip address you would like to scan?")
        startPort= input("What is the port range you would like to start scanning on?(0-65,535)")
        endPort=input("What is the port you would like to end on? (0-65,535)")
        scanIP(targetIP, startPort, endPort)
    elif mode== "2":
        cidrBlock=input("Enter the IP address block you would like to scan.   ")
        buildIPArray(cidrBlock)
main()