#!/usr/bin/env python3
###########################
# Title: OpsChallenge02
# Author:Jeff Snyder
# Date: 12OCT2020
# Purpose:Encrypt/Decrypt a File or message 
###########################

import smtplib
from cryptography.fernet import Fernet

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

def encrypt_message(message):
    """
    Encrypts a message
    """
    key = load_key()
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)

    print(encrypted_message)

def decrypt_message(encrypted_message):
    """
    Decrypts an encrypted message
    """
    key = load_key()
    f = Fernet(key)
    message = f.decrypt(encrypted_message)

    print(message)

def main():
    global key
    print("1. Encrypt a file \n2. Decrypt a file  \n3. Encrypt a message \n4. Decrypt a message")
    mode=input("Which mode would you like to run? Choose 1-4:  ")
    print("mode is:", mode)
    if mode== "1":
        generate_key()
        print("You have chosen 1")
        fileLocation=input("You have chosen mode 1.  \nPlease type the location of the file you would like to encrypt:  ")
        encrypt(fileLocation)
    elif mode== "2":
        print("You have chosen mode 2")
        fileLocation=input("You have chosen mode 2.  \nPlease type the location of the file you would like to decrypt:  ")
        decrypt(fileLocation)
    elif mode== "3":
        generate_key()
        print("You have chosen mode3")
        message=input("You have chosen mode 3.  \nPlease type the message you would like to encrypt:  ")
        encrypt_message(message)
    elif mode== "4":
        print("You have chosen mode4")
        encrypted_message=input("You have chosen mode 4.  \nPlease type the message you would like to decrypt:  ")
        decrypt_message(encrypted_message)
main()


# help from https://devqa.io/encrypt-decrypt-data-python/
# help from https://www.thepythoncode.com/article/encrypt-decrypt-files-symmetric-python