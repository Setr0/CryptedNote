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
root.resizable(False, False)
root.geometry(f"{windowWidth}x{windowHeight}+{int(monitorWidth/2-windowWidth/2)}+{int(monitorHeight/2-windowHeight/2)}")

rootFrame = ctk.CTkFrame(root)