ALPHABET = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def decryption(cipher_text, key):
    cipher_text = cipher_text.upper()
    key = key.upper()
    key_index = 0
    plain_text = ""
    for character in cipher_text:
        index = (ALPHABET.find(character) - ALPHABET.find(key[key_index])) % len(ALPHABET)
        plain_text = plain_text + ALPHABET[index]
        key_index += key_index
        if key_index == len(key):
            key_index = 0
    return plain_text

cp_text = input("Enter the cipher text: ")
key = input("Enter the key for decryption: ")
print(decryption(cp_text, key))