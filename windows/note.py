import customtkinter as ctk
from windows.root import root
from func.note import exitNote

noteFrame = ctk.CTkFrame(root, fg_color="transparent")

navbarFrame = ctk.CTkFrame(noteFrame, fg_color="transparent")
navbarFrame.pack(fill=ctk.X)

saveButton = ctk.CTkButton(navbarFrame, text="Save", width=80, font=("Helvetica", 15))
saveButton.pack(side=ctk.LEFT)

exitButton = ctk.CTkButton(navbarFrame, text="Exit", width=80, font=("Helvetica", 15), command=exitNote)
exitButton.pack(side=ctk.RIGHT)

textarea = ctk.CTkTextbox(noteFrame, font=("Helvetica", 20))
textarea.pack(expand=True, fill=ctk.BOTH)