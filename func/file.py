JSON_FILE = "json/notes.json"

def read():
    fileReader = open(JSON_FILE, "r")

    return fileReader.read()


def write(text):
    fileWriter = open(JSON_FILE, "w")
    
    fileWriter.write(text)
    fileWriter.close
