from windows.root import root
from func.note import create
from func.theme import getTheme, changeTheme
import customtkinter as ctk

homeFrame = ctk.CTkFrame(root, fg_color="transparent")

newNoteFormFrame = ctk.CTkFrame(homeFrame, fg_color="transparent")
newNoteFormFrame.pack(pady=20)

titleEntry = ctk.CTkEntry(newNoteFormFrame, width=500, height=40, font=("Helvetica", 20), placeholder_text="Title")
titleEntry.grid(row=0, column=0)

newNoteButton = ctk.CTkButton(newNoteFormFrame,
                                text="New",
                                width=70,
                                height=40,
                                font=("Helvetica", 20), 
                                command=lambda:create(titleEntry))

newNoteButton.grid(row=0, column=1, padx=(10, 0))

notesFrame = ctk.CTkScrollableFrame(homeFrame, fg_color="transparent")
notesFrame.pack(pady=20, fill=ctk.BOTH, expand=True)

themeButton = ctk.CTkButton(homeFrame, 
                            text=getTheme(), 
                            width=70, 
                            height=40, 
                            font=("Helvetica", 20), 
                            command=lambda: changeTheme(themeButton))
themeButton.pack(side=ctk.LEFT, anchor=ctk.SW)