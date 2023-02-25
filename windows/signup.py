import customtkinter as ctk
from windows.root import root
from func.creds import signup

signupFrame = ctk.CTkFrame(root, fg_color="transparent")

warningLabel = ctk.CTkLabel(signupFrame, text="YOU CAN'T CHANGE THE PASSWORD", text_color="red", font=("Babas Neue", 30, "bold"))
warningLabel.pack(pady=(0, 100))

passwordEntry = ctk.CTkEntry(signupFrame, placeholder_text="Password", width=500, height=40, font=("Helvetica", 20), show="*")
passwordEntry.pack()

confirmPasswordEntry = ctk.CTkEntry(signupFrame, placeholder_text="Confirm password", width=500, height=40, font=("Helvetica", 20), show="*")
confirmPasswordEntry.pack(pady=(20, 0))

createButton = ctk.CTkButton(signupFrame, 
                             text="Create password",
                             width=500, 
                             height=40, 
                             font=("Helvetica", 20),
                             command=lambda: signup(signupFrame, passwordEntry, confirmPasswordEntry))
createButton.pack(pady=(20, 0))