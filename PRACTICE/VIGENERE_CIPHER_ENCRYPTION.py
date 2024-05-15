ALPHABET = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encryption(plain_text, key):
    plain_text = plain_text.upper()
    key = key.upper()
    key_index = 0
    cipher_text =""
    for character in plain_text:
        index=(ALPHABET.find(character) + ALPHABET.find(key[key_index])) % len(ALPHABET)
        cipher_text = cipher_text + ALPHABET[index]
        key_index += key_index
        if key_index == len(key):
            key_index = 0
    return cipher_text

pl_text = input("Enter the plain text: ")
key = input("Enter the Encryption key: ")
print("Encrypted Text: ")
print(encryption(pl_text, key))