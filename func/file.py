def read(jsonFile):
    fileReader = open(jsonFile, "r")

    return fileReader.read()

def write(jsonFile, text):
    fileWriter = open(jsonFile, "w")
    
    fileWriter.write(text)
    fileWriter.close
