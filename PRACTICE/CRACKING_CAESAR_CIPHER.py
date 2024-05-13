ALPHABET=" ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def caesar_crack(cipher_text):
    for i in range(len(ALPHABET)):
        plain_text=""
        for c in cipher_text:
            index=ALPHABET.find(c)
            index= (index-i) % len(ALPHABET)
            plain_text=plain_text+ALPHABET[index]
        print("the plain text for key ",i," is: ",plain_text)

cipher_text=input("Enter the cipher text")
caesar_crack(cipher_text)

# BRUTE-FORCE ATTACK METHOD