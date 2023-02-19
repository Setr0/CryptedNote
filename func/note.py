import customtkinter as ctk
import json
import func.crypt as crypt
import func.file as file

def create(titleEntry):
    from windows.home import homeFrame

    title = titleEntry.get()
    cryptedTitle = crypt.encrypt(title)

    notesObject = json.loads(file.read())

    if cryptedTitle in notesObject.keys():
        titleEntry.delete(0, ctk.END)
        return

    notesObject[cryptedTitle] = crypt.encrypt("")

    newNoteButton = ctk.CTkButton(homeFrame, 
                                  text=title, 
                                  width=500, 
                                  height=40, 
                                  font=("Helvetica", 20), 
                                  command=lambda:openNote(cryptedTitle))
    
    newNoteButton.pack(pady=20)
    titleEntry.delete(0, ctk.END)

    jsonFileWriter = open("./json/notes.json", "w")
    jsonFileWriter.write(json.dumps(notesObject, indent=4))
    jsonFileWriter.close()

def openNote(title):
    from windows.home import homeFrame
    from windows.note import noteFrame, textarea, saveButton, newTitleEntry

    homeFrame.pack_forget()
    noteFrame.pack(expand=True, fill=ctk.BOTH)
    saveButton.configure(command=lambda:save(title, textarea.get(1.0, "end")))

    notesObject = json.loads(file.read())

    decryptedText = crypt.decrypt(notesObject[title])

    textarea.insert(1.0, decryptedText)

    newTitleEntry.insert(0, crypt.decrypt(title))

def save(title, text):
    notesObject = json.loads(file.read())

    cryptedText = crypt.encrypt(text)

    notesObject[title] = cryptedText

    file.write(json.dumps(notesObject, indent=4))

def exitNote():
    from windows.home import homeFrame
    from windows.note import noteFrame, textarea

    textarea.delete(1.0, ctk.END)

    noteFrame.pack_forget()
    homeFrame.pack(fill=ctk.BOTH, expand=True)
