ENGLISH_WORDS = []

def get_data():

    dictionary = open('words.txt','r')
    for word in dictionary.read().split('\n'):
        ENGLISH_WORDS.append(word)
    
    dictionary.close()

def count_words(text):
    text = text.upper()
    words=text.split(' ')
    matches=0
    for word in words:
        if word in ENGLISH_WORDS:
            matches += 1
    
    return matches

def is_text_english(text):
    matches=count_words()
    if(float(matches)/len(text.split('\n'))) * 100 >= 80:
        return True
    
