from windows.root import root
import func.note as note
from func.text import check
import customtkinter as ctk

noteFrame = ctk.CTkFrame(root, fg_color="transparent")

navbarFrame = ctk.CTkFrame(noteFrame, fg_color="transparent")
navbarFrame.pack(fill=ctk.X)

navbarFrame.columnconfigure(0, weight=1)
navbarFrame.columnconfigure(1, weight=1)

saveButton = ctk.CTkButton(navbarFrame, 
                           bg_color="transparent", 
                           text="Save", 
                           width=80, 
                           height=40, 
                           font=("Helvetica", 20), 
                           command=lambda: note.save(oldTitleVariable.get(), textarea.get(1.0, "end")))
saveButton.grid(column=0, row=0, sticky=ctk.W, padx=5, pady=5)

newTitleForm = ctk.CTkFrame(navbarFrame, fg_color="transparent")
newTitleForm.grid(column=1, row=0, sticky=ctk.NW, pady=5)

oldTitleVariable = ctk.StringVar()

newTitleEntry = ctk.CTkEntry(newTitleForm, width=500, height=40, font=("Helvetica", 20), placeholder_text="New title")
newTitleEntry.grid(row=0, column=0)

newTitleButton = ctk.CTkButton(newTitleForm, 
                                text="New",
                                width=70,
                                height=40,
                                font=("Helvetica", 20),
                                command=lambda: note.newTitle(oldTitleVariable.get(), newTitleEntry.get()))
newTitleButton.grid(row=0, column=1, padx=(10, 0))

exitButton = ctk.CTkButton(navbarFrame, text="Exit", width=80, height=40, font=("Helvetica", 20), command=note.exitNote)
exitButton.grid(column=2, row=0, padx=5, pady=5, sticky=ctk.E)

deleteButton = ctk.CTkButton(navbarFrame, 
                             text="Delete", 
                             width=80, 
                             height=40, 
                             font=("Helvetica", 20), 
                             command=lambda: note.deleteNote(oldTitleVariable.get()))
deleteButton.grid(column=3, row=0, padx=5, pady=5, sticky=ctk.E)

textarea = ctk.CTkTextbox(noteFrame, font=("Helvetica", 20))
textarea.pack(expand=True, fill=ctk.BOTH)

textarea.bind("<KeyRelease>", lambda event: check(textarea, wordsLabel, charsLabel))

infoBar = ctk.CTkFrame(noteFrame, height=40)
infoBar.pack(fill=ctk.X, side=ctk.BOTTOM)

charsLabel = ctk.CTkLabel(infoBar, text="Characters: 0", font=("Helvetica", 20))
charsLabel.pack(side=ctk.LEFT, padx=(20, 0))
text = textarea.get(1.0, "end-1c")
charsLabel.configure(text=f"Characters: {len(text)}")

wordsLabel = ctk.CTkLabel(infoBar, text="Words: 0", font=("Helvetica", 20))
wordsLabel.pack(side=ctk.LEFT, padx=(20, 0))