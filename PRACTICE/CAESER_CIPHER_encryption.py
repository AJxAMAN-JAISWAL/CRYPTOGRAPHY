ALPHABET=" ABCDEFGHIJKLMNOPQRSTUVWXYZ"
KEY=input("Enter the key for CAESAR CIPHER: \n")
key=int(KEY)

def caesar_encryption(plain_text):
    cipher_text=""
    plain_text=plain_text.upper()
    for c in plain_text:
        index=ALPHABET.find(c)
        index = (index + key) % len(ALPHABET)
        cipher_text=cipher_text + ALPHABET[index]

    return cipher_text

plain_text=input("Enter the text to be encrypted : \n")
print(caesar_encryption(plain_text))