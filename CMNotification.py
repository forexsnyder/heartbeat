#!/usr/bin/env python3
###########################
# Title: OpsChallenge02
# Author:Jeff Snyder
# Date: 07OCT2020
# Purpose:Create a constant ping to an IP Address
###########################
import smtplib
import email.utils
import os, datetime, time

#variables
gmail_user= input("Your email address: ")
gmail_password= input("your password: ")

msg= "Hello, World!"
sender="jeff@gmail.com"
destAddress="jeffcodefellows@gmail.com"

now= datetime.datetime.now()
pop= input("Enter IP Address:")
pingState= 1


#function
def emailMessage(msg):
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sender, destAddress, msg)
        server.quit()
        print ('Email sent!')
    except:
        print ('Something went wrong...')



def pinging():
    global pingState
    ping= os.system ("ping -c 1 " + str(pop))
    #connetion is good
    if ping== 0:
        if (pingState== 0):
            address= str(pop)
            # msg = "Testing the first string"
            msg= f"At {now:%H%M} on {now:%B %d, %Y} {pop} went from down to up."
            emailMessage(msg)
        time.sleep( 2 )
        pingState=1
        pinging()
    #connection is bad
    else:
        if (pingState== 1):
            address= str(pop)
            # msg = "Testing this string"
            msg= f"At {now:%H%M} on {now:%B %d, %Y} {pop} went from up to down."
            # print (msg)
            emailMessage(msg)
        time.sleep( 5 )
        pingState= 0
        pinging()
 
        
pinging()