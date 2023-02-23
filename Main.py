from windows.root import root
from windows.signup import signupFrame
from windows.login import loginFrame
import customtkinter as ctk
import json
from os.path import exists
from func.note import openNote
from func.crypt import decrypt
import func.file as file

if __name__ == "__main__":
    if not exists("json/notes.json"):
        file.write("json/notes.json", json.dumps({}, indent=4))

    if exists("json/creds.json"):
        loginFrame.pack(expand=True)
    else:
        signupFrame.pack(expand=True)

    root.mainloop()
