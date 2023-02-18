from windows.home import homeFrame
from windows.root import root
import customtkinter as ctk
import json
from func.note import openNote
from cryptography.fernet import Fernet

key = "0iMZOpJiqgarAptwwEkd3l2PH6wBkfLC1RFQgpmLiC8="
fernet = Fernet(key)

if __name__ == "__main__":
    homeFrame.pack(fill=ctk.BOTH, expand=True)

    jsonFileReader = open("./json/notes.json", "r")
    notesObject = json.loads(jsonFileReader.read())
    notes = list(notesObject.keys())

    notes.sort()

    for note in notes:
        title = str(fernet.decrypt(note).decode())

        newNoteButton = ctk.CTkButton(homeFrame, 
                                  text=title, 
                                  width=500, 
                                  height=40, 
                                  font=("Helvetica", 20), 
                                  command=lambda:openNote(note))
        
        newNoteButton.pack(pady=20)

    root.mainloop()
