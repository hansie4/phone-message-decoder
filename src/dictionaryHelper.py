
class DecodingDict(dict):

    def __init__(self):
        dict.__init__(self)

    def isWordInDict(self, wordToFind):
        for word in self.get(wordToFind[0].upper()):
            if(word == wordToFind.upper()):
                return True
        return False


def loadWordDict(fileToLoadWordsFrom):
    dictionary = initalizeDictionary()
    words = list()
    with open(fileToLoadWordsFrom) as words_file:
        words = words_file.readlines()

    for index in range(len(words)):
        dictionary.get(words[index][0].upper()).append(
            words[index].strip().upper())

    return dictionary


def initalizeDictionary():
    initialDict = DecodingDict()

    for i in range(26):
        initialDict.update({chr(i + 65): list()})

    return initialDict
