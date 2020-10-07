#!/usr/bin/env python3
###########################
# Title: OpsChallenge02
# Author:Jeff Snyder
# Date: 06OCT2020
# Purpose:Create a constant ping to an IP Address
###########################
import os, datetime, time

#variables
now= datetime.datetime.now()
pop= input("Enter IP Address:")

#function
def pinging():
    ping= os.system ("ping -c 1 " + str(pop))
    if ping== 0:
        print (str(now) + " Network Active to " + pop)
        print ("Waiting 5 seconds to ping again or press control + C to exit")
        time.sleep( 5 )
        pinging()
    else:
        print ("There was an error, or network is down")
        print ("Waiting 5 seconds and then will try again")
        print ("or press Control + C to exit")
        time.sleep( 5 )
        pinging()

pinging()