from windows.home import homeFrame, notesFrame
from windows.root import root
import customtkinter as ctk
import json
from func.note import openNote
from func.crypt import decrypt
from func.file import read

if __name__ == "__main__":
    homeFrame.pack(fill=ctk.BOTH, expand=True)
    
    notesObject = json.loads(read())
    notes = list(notesObject.keys())

    notes.sort()

    if len(notes) > 0:
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
