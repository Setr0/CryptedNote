import customtkinter as ctk
from windows.root import root

noteFrame = ctk.CTkFrame(root, fg_color="transparent")

saveButton = ctk.CTkButton(noteFrame, text="Save", width=80, font=("Helvetica", 15))
saveButton.pack(side=ctk.TOP, anchor=ctk.NW)

textarea = ctk.CTkTextbox(noteFrame, font=("Helvetica", 20))
textarea.pack(expand=True, fill=ctk.BOTH)