from windows.home import homeFrame
from windows.root import root
import customtkinter as ctk

if __name__ == "__main__":
    homeFrame.pack(fill=ctk.BOTH, expand=True)

    root.mainloop()
