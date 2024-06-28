#################################################################################################
#This is a practice program to try and encrypt a txt file, and then decrypt it                  #
#coder: Eilifir                                                                                 #
#################################################################################################
from cryptography.fernet import Fernet
import os
file1 = open ("password.txt", "a+")
file_path = os.getcwd() + "\password.txt"
file_size = os.path.getsize(file_path)

if file_size == 0:
    key = Fernet.generate_key()                     #Generate the key to encrypt and decrypt
    file1.write("{} \n".format(key))
    print("{}".format(key))
else:
    file1 = open("password.txt", "r+")
    data = file1.readline(-1)
    data = data.replace("b'", "", 1)
    data = data.replace("'", "")
    data = data.replace(" \n", "")
    salt = data.encode("utf-8")
    key = salt
f = Fernet(key)
password = input()
password = password.encode("utf-8")
token = f.encrypt(password)
file1.write("{} \n".format(token))

