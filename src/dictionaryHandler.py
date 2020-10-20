

def loadWords(fileToLoadWordsFrom):
    with open(fileToLoadWordsFrom) as word_file:
        words = set(line.strip() for line in open(fileToLoadWordsFrom))
    return words
