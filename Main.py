from windows.home import homeFrame, notesFrame
from windows.root import root
import customtkinter as ctk
import json
from os.path import exists
from func.note import openNote
from func.crypt import decrypt
import func.file as file

if __name__ == "__main__":

    if not exists("json/notes.json"):
        file.write(json.dumps({}, indent=4))

    homeFrame.pack(fill=ctk.BOTH, expand=True)
    
    notesObject = json.loads(file.read())
    notes = list(notesObject.keys())

    notes.sort()

    for note in notes:
        title = decrypt(note)

        newNoteButton = ctk.CTkButton(notesFrame, 
                                    text=title, 
                                    width=500, 
                                    height=40, 
                                    font=("Helvetica", 20), 
                                    command=lambda:openNote(note))
            
        newNoteButton.pack(pady=20)

    root.mainloop()
