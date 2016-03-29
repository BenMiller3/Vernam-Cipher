"""
Vernam Cipher
Benjamin D. Miller
Takes a key, and a message
Encripts the message using the key
"""
def vernam(key,message):
    m = message.upper().replace(" ","") # Convert to upper case, remove whitespace
    encrypt = ""
    
    for i in range(len(m)):
        letter = ord(m[i])-65      # Letters now range 0-25
        letter = (letter + key)%25 # Alphanumeric + key mod 25 = 0-25
        letter +=65
        

        encrypt = encrypt + chr(letter) # Concatenate message
        
    return encrypt

""" * TEST CASES * """
vernam(9,"hello world")
vernam(14,"WHO R U")
