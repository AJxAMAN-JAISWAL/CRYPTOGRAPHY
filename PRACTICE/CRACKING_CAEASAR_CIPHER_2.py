import matplotlib.pylab as plt

ALPHABET="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def frequency_analysis(cipher_text):
    cipher_text=cipher_text.upper()
    letter_frequencies={}
    for letter in ALPHABET:
        letter_frequencies[letter]=0
    
    for letter in cipher_text:
        if letter in ALPHABET:
            letter_frequencies[letter]+=1
    return letter_frequencies

def plot_Distribution(frequencies):
    plt.bar(frequencies.keys(),frequencies.values())
    plt.show()

def caesar_crack(cipher_text):
    freq=frequency_analysis(cipher_text)
    freq=sorted(freq.items(), key=lambda x: x[1], reverse=True)
    print("The possible key value: %s" % (ALPHABET.find(freq[0][0]) - ALPHABET.find('E')))

cipher_text=input("Enter a cipher text for frequency analysis: \n")
fq=frequency_analysis(cipher_text)
plot_Distribution(fq)
caesar_crack(cipher_text)