from windows.home import homeFrame
from windows.root import root
import customtkinter as ctk
import json
from func.note import openNote

if __name__ == "__main__":
    homeFrame.pack(fill=ctk.BOTH, expand=True)

    jsonFileReader = open("./json/notes.json", "r")
    notesObject = json.loads(jsonFileReader.read())
    notes = notesObject.keys()

    for note in notes:
        newNoteButton = ctk.CTkButton(homeFrame, 
                                  text=note, 
                                  width=500, 
                                  height=40, 
                                  font=("Helvetica", 20), 
                                  command=lambda:openNote(note))
        
        newNoteButton.pack(pady=20)

    root.mainloop()
