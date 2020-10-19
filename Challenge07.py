
#!/usr/bin/env python3
###########################
# Title: OpsChallenge02
# Author:Jeff Snyder
# Date: 18OCT2020
# Purpose:Encrypt/Decrypt a Folder Recursively
###########################


import os
from cryptography.fernet import Fernet
import smtplib

def generate_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """
    Load the previously generated key
    """
    return open("secret.key", "rb").read()

def folderEncrypt(fileLocation):
        path = fileLocation
        files = []

    # r=root, d=directories, f = files
        for r, d, f in os.walk(path):
                for file in f:
                        files.append(os.path.join(r, file))

        for f in files:
                print(f)
                encrypt(f)

def folderDecrypt(fileLocation):
        path = fileLocation
        files = []

    # r=root, d=directories, f = files
        for r, d, f in os.walk(path):
                for file in f:
                        files.append(os.path.join(r, file))

        for f in files:
                print(f)
                decrypt(f)

def encrypt(fileLocation):
    key = load_key()
    """
    Given a fileLocation (str) and key (bytes), it encrypts the file and write it
    """
    f = Fernet(key)
    with open(fileLocation, "rb") as file:
        # read all file data
        file_data = file.read()
    # encrypt data
    encrypted_data = f.encrypt(file_data)
    # write the encrypted file
    with open(fileLocation, "wb") as file:
        file.write(encrypted_data)

        
def decrypt(fileLocation): 
    """
    Given a fileLocation (str) and key (bytes), it decrypts the file and write it
    """
    key = load_key()
    f = Fernet(key)
    with open(fileLocation, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(fileLocation, "wb") as file:
        file.write(decrypted_data)

def main():
    print("1. Encrypt a folder \n2. Decrypt a folder")
    mode=input("Which mode would you like to run? Choose 1-2:  ")
    print("mode is:", mode)
    if mode== "1":
        generate_key()
        print("You have chosen 1")
        fileLocation=input("You have chosen mode 1.  \nPlease type the location of the folder you would like to encrypt:  ")
        folderEncrypt(fileLocation)
    elif mode== "2":
        print("You have chosen mode 2")
        fileLocation=input("You have chosen mode 2.  \nPlease type the location of the folder you would like to decrypt:  ")
        folderDecrypt(fileLocation)
main()