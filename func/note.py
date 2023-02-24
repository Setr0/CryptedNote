from func.text import check
import customtkinter as ctk
import func.crypt as crypt
import func.file as file
import json

def create(titleEntry):
    from windows.home import notesFrame

    title = titleEntry.get()
    
    cryptedTitle = crypt.encrypt(title)

    notesObject = json.loads(file.read("json/notes.json"))

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

    file.write("json/notes.json", json.dumps(notesObject, indent=4))

def openNote(title):
    from windows.home import homeFrame, notesFrame
    import windows.note as noteWindow

    for child in notesFrame.winfo_children():
        child.destroy()

    homeFrame.pack_forget()

    noteWindow.noteFrame.pack(expand=True, fill=ctk.BOTH)
    noteWindow.oldTitleVariable.set(title)

    notesObject = json.loads(file.read("json/notes.json"))

    decryptedText = crypt.decrypt(notesObject[title])

    noteWindow.textarea.insert(1.0, decryptedText)
    noteWindow.newTitleEntry.insert(0, crypt.decrypt(title))
    check(noteWindow.textarea, noteWindow.wordsLabel, noteWindow.charsLabel)

def save(title, text):
    notesObject = json.loads(file.read("json/notes.json"))

    cryptedText = crypt.encrypt(text)

    notesObject[title] = cryptedText

    file.write("json/notes.json", json.dumps(notesObject, indent=4))

def exitNote():
    from func.home import openHome
    from windows.note import noteFrame, textarea, newTitleEntry

    textarea.delete(1.0, ctk.END)

    newTitleEntry.delete(0, ctk.END)

    openHome(noteFrame)

def newTitle(oldTitle, newTitle):
    from windows.note import oldTitleVariable

    notesObject = json.loads(file.read("json/notes.json"))

    cryptedNewTitle = crypt.encrypt(newTitle)
    notesObject[cryptedNewTitle] = notesObject[oldTitle]

    del notesObject[oldTitle]

    file.write("json/notes.json", json.dumps(notesObject, indent=4))

    oldTitleVariable.set(cryptedNewTitle)

def deleteNote(title):
    notesObject = json.loads(file.read("json/notes.json"))

    del notesObject[title]

    file.write("json/notes.json", json.dumps(notesObject, indent=4))

    exitNote()
    