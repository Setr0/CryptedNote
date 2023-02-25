import func.file as file
import customtkinter as ctk
import json

def getTheme():
    themeStrObject = file.read("json/theme.json")
    themeObject = json.loads(themeStrObject)
    theme = themeObject["theme"]

    return theme


def changeTheme(button):
    currentTheme = button.cget("text")
    newTheme = "System"

    if currentTheme == "Light":
        newTheme = "Dark"
    else:
        newTheme = "Light"

    ctk.set_appearance_mode(newTheme)

    button.configure(text=newTheme)

    file.write("json/theme.json", json.dumps({"theme": newTheme}, indent=4))
    