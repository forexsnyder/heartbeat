import smtplib
import random
import itertools
import sys
import time
# # filepath=""   
# filePath=open(input("Please enter the file location of the dictionary."),'r')
# i=0
# length = len(filePath)
# while i <length:
#     password=i
#     print(filePath[i])
#     i +=1
filepath = '/home/jeff/Desktop/sample.txt'
passwordCheck="password"
with open(filepath) as fp:
    line = fp.readline()
    cnt = 1
    while line:
        line=line.strip()
        print(line)
        if line == passwordCheck:
            print("Your password of {} is a match in the dictionary".format(passwordCheck))
            break
        else:
            print("{}".format(line.strip()))
            line = fp.readline()
            time.sleep(1)
            cnt += 1