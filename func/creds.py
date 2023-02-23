from func.home import openHome
import json
import customtkinter as ctk
import func.file as file
import func.crypt as crypt

def signup(signupFrame, passwordEntry, confirmPasswordEntry):
    password = passwordEntry.get()
    confirmPassword = confirmPasswordEntry.get()

    if len(password) == 0 and len(confirmPassword) == 0:
        return
    
    if password != confirmPassword:
        confirmPasswordEntry.delete(0, ctk.END)

        return

    cryptedPassword = crypt.encrypt(password)

    credsObj = {
        "password": cryptedPassword
    }

    file.write("json/creds.json", json.dumps(credsObj, indent=4))

    openHome(signupFrame)


def login(loginFrame, passwordEntry):
    password = passwordEntry.get()
    
    creds = file.read("json/creds.json")
    credsObj = json.loads(creds)
    realPasswordCrypted = credsObj["password"]
    realPassword = crypt.decrypt(realPasswordCrypted)

    if len(password) == 0:
        return

    if password != realPassword:
        passwordEntry.delete(0, ctk.END)

        return

    openHome(loginFrame)