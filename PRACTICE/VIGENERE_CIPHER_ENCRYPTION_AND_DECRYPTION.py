ALPHABET = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encryption(plain_text, key):
    plain_text = plain_text.upper()
    key = key.upper()
    key_index = 0
    cipher_text = ""
    for character in plain_text:
        index=(ALPHABET.find(character)+ALPHABET.find(key[key_index])) % len(ALPHABET)
        cipher_text=cipher_text + ALPHABET[index]
        key_index += key_index
        if key_index == len(key):
            key_index = 0
    return cipher_text

def decryption(cipher_text, key):
    cipher_text = cipher_text.upper()
    key = key.upper()
    plain_text = ""
    key_index = 0
    for character in cipher_text:
        index=(ALPHABET.find(character)-ALPHABET.find(key[key_index])) % len(ALPHABET)
        plain_text=plain_text + ALPHABET[index]
        key_index += key_index
        if key_index == len(key):
            key_index = 0
    return plain_text        

plain_text = input("Enter plain text: ")
key = input("Enter key for encryption: ")
print("Encrypted Text: ")
print(encryption(plain_text, key))
cipher_text = encryption(plain_text, key)
print("Decrypted Text: ")
print(decryption(cipher_text, key))