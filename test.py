from cryptography.fernet import Fernet
 
message = "hello geeks"
 
key = "0iMZOpJiqgarAptwwEkd3l2PH6wBkfLC1RFQgpmLiC8="
print(key)
 
fernet = Fernet(key)
 
encMessage = fernet.encrypt(message.encode())

print(str(encMessage).replace("'b", "").replace("'", ""))
 
print("original string: ", message)
print("encrypted string: ", encMessage)
 
decMessage = fernet.decrypt("gAAAAABj8OqMscP-U20YnOhxcjjsttakqhIrHjuxR5RngjJkkRMCUdB-VZUJZo1in6FkxqHKIVVDe3V5MDcisYskwvExHDdD5w==").decode()
 
print("decrypted string: ", decMessage)