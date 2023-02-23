import customtkinter as ctk
from windows.root import root
from func.creds import login

loginFrame = ctk.CTkFrame(root, fg_color="transparent")

passwordEntry = ctk.CTkEntry(loginFrame, placeholder_text="Password", width=500, height=40, font=("Helvetica", 20), show="*")
passwordEntry.pack()

accessButton = ctk.CTkButton(loginFrame, 
                             text="Access",
                             width=500, 
                             height=40, 
                             font=("Helvetica", 20),
                             command=lambda: login(loginFrame, passwordEntry))
accessButton.pack(pady=(20, 0))