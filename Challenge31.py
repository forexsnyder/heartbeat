#!/usr/bin/env python3
###########################
# Title: OpsChallenge31
# Author:Jeff Snyder
# Date: 16NOV2020
# Purpose: Search for file
# With help from https://stackoverflow.com/questions/1724693/find-a-file-in-python
###########################


import os, fnmatch
def scanWindows(fileDirectory, fileName):
    results=[]
    for paths, subdirs, files in os.walk(start_dir, topdown=True):
    for file in files:
        full_path = os.path.join(paths, file)
        normalised = os.path.normpath(full_path)
        print(normalised)


def scanLinux(fileDirectory, fileName):
    results=[]
    for root, dirs, files in os.walk(fileDirectory):
        for name in files:
            if fnmatch.fnmatch(name, fileName):
                results.append(os.path.join(root, name))
    return print(results)


def main():
    print("Shall we play a game?")
    mode=input("What operating system are you using? Press 1. For Windows. 2. For Linux:  ")

    if mode == "1":
        fileDirectory=input("What is the file directory path you would like to scan?   ")
        fileName=input("What is the file name you would like to search for?  ")
        scanWindows(fileDirectory,fileName)
    if mode =="2":
        fileDirectory=input("What is the file directory path you would like to scan?   ")
        fileName=input("What is the file name you would like to search for?  ")
        scanLinux(fileDirectory,fileName)

main()
