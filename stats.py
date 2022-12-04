

def calc_occurrences(words):
    word_occurences = {}

    for word in words:
        if word not in word_occurences.keys():
            word_occurences[word] = 1
        else:
            word_occurences[word] += 1
    
    return word_occurences