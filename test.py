#!/usr/bin/env python
import zipfile
import itertools


txtFile="/home/jeff/sample.txt"
zip_file="test1.zip"
zip_file=zipfile.ZipFile(zip_file)
filepath=open(txtFile)
for i in filepath.readlines():
    secret=i.strip()
    print(secret)
    try:
        zip_file.extractall(pwd=bytes(secret,"utf-8"))
    except:
        continue    
    else:
        print("Password is "+ secret)
        exit(0)
            
print("not found")