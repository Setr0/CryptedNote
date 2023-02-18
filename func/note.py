import customtkinter as ctk
import json
from cryptography.fernet import Fernet

key = "0iMZOpJiqgarAptwwEkd3l2PH6wBkfLC1RFQgpmLiC8="
fernet = Fernet(key)

def create(titleEntry):
    from windows.home import homeFrame

    title = titleEntry.get()
    cryptedTitle = str(fernet.encrypt(title.encode())).replace("b'", "").replace("'", "")

    jsonFileReader = open("./json/notes.json", "r")
    notesObject = json.loads(jsonFileReader.read())

    if cryptedTitle in notesObject.keys():
        titleEntry.delete(0, ctk.END)
        return

    notesObject[cryptedTitle] = str(fernet.encrypt("".encode())).replace("b'", "").replace("'", "")

    newNoteButton = ctk.CTkButton(homeFrame, 
                                  text=title, 
                                  width=500, 
                                  height=40, 
                                  font=("Helvetica", 20), 
                                  command=lambda:openNote(cryptedTitle))
    
    newNoteButton.pack(pady=20)
    titleEntry.delete(0, ctk.END)

    jsonFileWriter = open("./json/notes.json", "w")
    jsonFileWriter.write(json.dumps(notesObject))
    jsonFileWriter.close()

def openNote(title):
    from windows.home import homeFrame
    from windows.note import noteFrame, textarea, saveButton

    homeFrame.pack_forget()
    noteFrame.pack(expand=True, fill=ctk.BOTH)
    saveButton.configure(command=lambda:save(title, textarea.get(1.0, "end")))

    jsonFileReader = open("./json/notes.json", "r")
    notesObject = json.loads(jsonFileReader.read())

    decryptedText = str(fernet.decrypt(notesObject[title]).decode())

    textarea.insert(1.0, decryptedText)

def save(title, text):
    jsonFileReader = open("./json/notes.json", "r")
    notesObject = json.loads(jsonFileReader.read())

    cryptedText = str(fernet.encrypt(text.encode())).replace("b'", "").replace("'", "")

    notesObject[title] = str(cryptedText)

    jsonFileWriter = open("./json/notes.json", "w")
    jsonFileWriter.write(json.dumps(notesObject))
    jsonFileWriter.close()

def exitNote():
    from windows.home import homeFrame
    from windows.note import noteFrame, textarea

    textarea.delete(1.0, ctk.END)

    noteFrame.pack_forget()
    homeFrame.pack(fill=ctk.BOTH, expand=True)
