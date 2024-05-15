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


def caesar_crack(cipher_text):
    freq = frequency_analysis(cipher_text)
    freq_sorted = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    
    # Find the most common letter(s)
    most_common_letters = [freq_sorted[0][0]]
    max_frequency = freq_sorted[0][1]
    
    # Check if there are any ties in frequency
    for letter, frequency in freq_sorted[1:]:
        if frequency == max_frequency:
            most_common_letters.append(letter)
        else:
            break
    
    # Calculate the possible key(s)
    possible_keys = []
    for common_letter in most_common_letters:
        possible_keys.append(ALPHABET.find(common_letter) - ALPHABET.find('E'))
    
    print("The possible key value(s):", possible_keys)

cipher_text = input("Enter a cipher text for frequency analysis: \n")
caesar_crack(cipher_text)
