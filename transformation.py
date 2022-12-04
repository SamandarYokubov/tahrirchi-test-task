

def get_words(text):
    words = text.split(" ")
    symbols = ['.', '?', ',', '!', ':', '\\', '-', '»', '«']
    words = [word for word in words if len(word) > 2]
    for i, word in enumerate(words):
        if word[0] in symbols:
            words[i] = words[i].replace(word[0], '')
        elif word[-1] in symbols:
            words[i] = words[i].replace(word[-1], '') 
        words[i] = words[i].lower()
    return words