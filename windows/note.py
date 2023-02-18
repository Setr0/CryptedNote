import customtkinter as ctk
from windows.root import root

noteFrame = ctk.CTkFrame(root, fg_color="transparent")

textarea = ctk.CTkTextbox(noteFrame, font=("Helvetica", 20))
textarea.pack(expand=True, fill=ctk.BOTH)