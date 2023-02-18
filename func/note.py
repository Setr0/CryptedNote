import customtkinter as ctk
import json

def create(titleEntry):
    from windows.home import homeFrame

    title = titleEntry.get()
    jsonFileReader = open("./json/notes.json", "r")
    notesObject = json.loads(jsonFileReader.read())

    if title in notesObject.keys():
        titleEntry.delete(0, ctk.END)
        return

    notesObject[title] = ""

    newNoteButton = ctk.CTkButton(homeFrame, 
                                  text=title, 
                                  width=500, 
                                  height=40, 
                                  font=("Helvetica", 20), 
                                  command=lambda:openNote(title))
    
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

    textarea.insert(1.0, notesObject[title])

def save(title, text):
    jsonFileReader = open("./json/notes.json", "r")
    notesObject = json.loads(jsonFileReader.read())

    notesObject[title] = text

    jsonFileWriter = open("./json/notes.json", "w")
    jsonFileWriter.write(json.dumps(notesObject))
    jsonFileWriter.close()
