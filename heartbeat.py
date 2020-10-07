#!/usr/bin/python
import os, datetime, time

pop= input("Enter IP Address:")
interval= input("Enter time interval in seconds:")
ping= os.system ("ping " + str(pop))
