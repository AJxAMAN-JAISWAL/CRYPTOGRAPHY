ALPHABET = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
KEY=input("Enter the key which was entered during encryption :\n")
key=int(KEY)

def caesar_decryption(cipher_text):
    plain_text=""
    for c in cipher_text:
        index=ALPHABET.find(c)
        index = (index - key) % len(ALPHABET)
        plain_text=plain_text+ALPHABET[index]
    return plain_text

cipher_text=input("Enter the cipher text to be decrypted:\n")
print(caesar_decryption(cipher_text))