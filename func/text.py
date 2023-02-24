def check(textarea, wordsLabel, charsLabel):
    signs = ",.-_'\"*"

    text = textarea.get(1.0, "end-1c")
    text = text.replace("\n", " ")

    textArray = text.split(" ")

    while "" in textArray:
        textArray.remove("")

    while "\n" in textArray:
        textArray.remove("\n")

    wordsArray = textArray
    charsArray = textArray
    
    for sign in signs:
        while sign in wordsArray:
            wordsArray.remove(sign)

    wordsLabel.configure(text=f"Words: {len(textArray)}")
    
    for char in text:
        if char == " " or char == "\n":
            text = text.replace(char, "")
    
    charsArray = list(text)

    charsLabel.configure(text=f"Characters: {len(charsArray)}")
    