import customtkinter as ctk
import json
import func.crypt as crypt
import func.file as file

def create(titleEntry):
    from windows.home import notesFrame

    title = titleEntry.get()
    
    cryptedTitle = crypt.encrypt(title)

    notesObject = json.loads(file.read())

    if cryptedTitle in notesObject.keys() or len(title) == 0:
        titleEntry.delete(0, ctk.END)
        return

    notesObject[cryptedTitle] = crypt.encrypt("")

    newNoteButton = ctk.CTkButton(notesFrame, 
                                  text=title, 
                                  width=500, 
                                  height=40, 
                                  font=("Helvetica", 20), 
                                  command=lambda:openNote(cryptedTitle))
    newNoteButton.pack(pady=20)
    titleEntry.delete(0, ctk.END)

    file.write(json.dumps(notesObject, indent=4))

def openNote(title):
    from windows.home import homeFrame, notesFrame
    from windows.note import noteFrame, textarea, saveButton, newTitleEntry, deleteButton, newTitleButton, oldTitleVariable, checkText

    for child in notesFrame.winfo_children():
        child.destroy()

    homeFrame.pack_forget()
    noteFrame.pack(expand=True, fill=ctk.BOTH)
    saveButton.configure(command=lambda:save(oldTitleVariable.get(), textarea.get(1.0, "end")))
    deleteButton.configure(command=lambda:deleteNote(title))
    
    oldTitleVariable.set(title)
    newTitleButton.configure(command=lambda:newTitle(oldTitleVariable.get(), newTitleEntry.get()))

    notesObject = json.loads(file.read())

    decryptedText = crypt.decrypt(notesObject[title])

    textarea.insert(1.0, decryptedText)

    newTitleEntry.insert(0, crypt.decrypt(title))

    checkText()

def save(title, text):
    notesObject = json.loads(file.read())

    cryptedText = crypt.encrypt(text)

    notesObject[title] = cryptedText

    file.write(json.dumps(notesObject, indent=4))

def exitNote():
    from windows.home import homeFrame, notesFrame
    from windows.note import noteFrame, textarea, newTitleEntry

    textarea.delete(1.0, ctk.END)

    newTitleEntry.delete(0, ctk.END)

    noteFrame.pack_forget()
    homeFrame.pack(fill=ctk.BOTH, expand=True)

    notesObject = json.loads(file.read())

    notes = list(notesObject.keys())

    notes.sort()

    for note in notes:
        title = crypt.decrypt(note)

        newNoteButton = ctk.CTkButton(notesFrame, 
                                  text=title, 
                                  width=500, 
                                  height=40, 
                                  font=("Helvetica", 20), 
                                  command=lambda:openNote(note))
        
        newNoteButton.pack(pady=20)


def newTitle(oldTitle, newTitle):
    from windows.note import oldTitleVariable

    notesObject = json.loads(file.read())

    cryptedNewTitle = crypt.encrypt(newTitle)

    notesObject[cryptedNewTitle] = notesObject[oldTitle]

    del notesObject[oldTitle]

    file.write(json.dumps(notesObject, indent=4))

    oldTitleVariable.set(cryptedNewTitle)

def deleteNote(title):
    notesObject = json.loads(file.read())

    del notesObject[title]

    file.write(json.dumps(notesObject, indent=4))

    exitNote()