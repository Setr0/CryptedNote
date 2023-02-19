from cryptography.fernet import Fernet

fernet = Fernet("0iMZOpJiqgarAptwwEkd3l2PH6wBkfLC1RFQgpmLiC8=")

def encrypt(text):
    return str(fernet.encrypt(text.encode())).replace("b'", "").replace("'", "")

def decrypt(cryptedText):
    return str(fernet.decrypt(cryptedText).decode())
