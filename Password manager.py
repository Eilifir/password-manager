import PySimpleGUI as sg
from cryptography.fernet import Fernet
import os
#Create UI
tab_layout1 = [    [sg.Text('Type password to add: '), sg.InputText()],
            [sg.Button('Add'), sg.Button('Exit')]
]

tab_layout2 = [    [sg.Text('Show password?')],
            [sg.Text('Type site for the password: ')],
            [sg.Text('Select Encryption: ')],
            [sg.Button('Yes'), sg.Button('Exit')]

]
layout = [[sg.TabGroup([[sg.Tab("add", tab_layout1), sg.Tab("show", tab_layout2)]]), [sg.Titlebar("Password Manager V 0.1")]]]
window = sg.Window('Window Title', layout)

#get file location + size to check for the key
file_path = os.getcwd() + "\password.txt"
file1 = open (file_path, "a+")
file_size = os.path.getsize(file_path)
if file_size == 0:
    key = Fernet.generate_key()                     #Generate the key to encrypt and decrypt
    file1.writelines("{} \n".format(key))
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
file1.close()

while True:
    
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit': # if user closes window or clicks cancel
        break

    if event == 'Add':
        
        password = values [0]
        password = password.encode("utf-8")
        token = f.encrypt(password)
        with open(file_path, "a+") as file:
            file.write("{}\n".format(token))
window.close()