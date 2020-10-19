from decoderHelper import *


def decodePhoneKeypadMessage():

    rawMessage = getValidMessageToDecode()

    rawMessagePartitioned = getPartitionedMessage(rawMessage)

    possibleWords = list()

    for word in rawMessagePartitioned:
        possibleWords.append(getAllStrings(word))

    # DEBUGGING
    currentWord = 1
    print("------------------------------------------")
    for words in possibleWords:
        print("\t\tWord " + str(currentWord))
        for word in words:
            print("".join(word))
        currentWord = currentWord + 1
    print("------------------------------------------")
