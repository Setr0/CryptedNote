import customtkinter as ctk
import screeninfo

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

monitorWidth = screeninfo.get_monitors()[0].width
monitorHeight = screeninfo.get_monitors()[0].height

windowWidth = 900
windowHeight = 600

root = ctk.CTk()
root.title("Crypted Note")
root.geometry(f"{windowWidth}x{windowHeight}+{int(monitorWidth/2-windowWidth/2)}+{int(monitorHeight/2-windowHeight/2)}")

rootFrame = ctk.CTkFrame(root)

newNoteFormFrame = ctk.CTkFrame(rootFrame, fg_color="transparent")
newNoteFormFrame.pack(pady=20 ,side=ctk.TOP)

titleEntry = ctk.CTkEntry(newNoteFormFrame, width=500, height=40, font=("Helvetica", 20))
titleEntry.grid(row=0, column=0)

newNoteButton = ctk.CTkButton(newNoteFormFrame, text="New", width=70, height=40, font=("Helvetica", 20))
newNoteButton.grid(row=0, column=1, padx=10)