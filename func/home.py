from windows.home import homeFrame, notesFrame
from func.note import openNote
import func.crypt as crypt
import func.file as file
import customtkinter as ctk
import json

def openHome(previousFrame):
    previousFrame.pack_forget()

    homeFrame.pack(fill=ctk.BOTH, expand=True)
        
    notesObject = json.loads(file.read("json/notes.json"))
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