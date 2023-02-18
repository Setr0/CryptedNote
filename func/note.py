import customtkinter as ctk

def create(titleEntry):
    from windows.home import homeFrame

    newNoteButton = ctk.CTkButton(homeFrame, 
                                  text=titleEntry.get(), 
                                  width=500, 
                                  height=40, 
                                  font=("Helvetica", 20), 
                                  command=lambda:open(titleEntry.get()))
    
    newNoteButton.pack(pady=20)
    titleEntry.delete(0, ctk.END)

def open(title):
    from windows.home import homeFrame
    from windows.note import noteFrame, textarea

    homeFrame.pack_forget()
    noteFrame.pack(expand=True, fill=ctk.BOTH)
