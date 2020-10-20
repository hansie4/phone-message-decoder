from collections import deque


def getValidMessageToDecode():
    validMessageRetrieved = False

    while (not validMessageRetrieved):
        rawMessage = input("Enter Message to Decode: ")
        if(isMessageToDecodeValid(rawMessage)):
            return rawMessage
        else:
            print(
                "The message you entered was invalid. The only characters should be digits 2-9 and '-'.")


def isMessageToDecodeValid(message):

    if(message):
        for character in message:
            if((character != '-') and (character != '2') and (character != '3') and (character != '4') and (character != '5') and (character != '6') and (character != '7') and (character != '8') and (character != '9')):
                return False

        return True
    else:
        return False


def getPartitionedMessage(message):
    return message.split("-")


def getAllPossibleWordPermutations(message):

    partitionedMessage = getPartitionedMessage(message)

    allWordCombinations = list()

    currentWordNumber = 1
    for digitSequence in partitionedMessage:

        totalPermutationsPossible = getNumberOfAllWordPermutations(
            digitSequence)
        processedPermutations = [0]

        possibleLettersForWordPermutationList = getPossibleLettersForWordPermutationList(
            digitSequence)

        wordPermutation = deque()
        wordPermutationsList = list()

        getAllPossibleWordPermutationsRec(
            possibleLettersForWordPermutationList, wordPermutation, wordPermutationsList, totalPermutationsPossible, processedPermutations, currentWordNumber)

        allWordCombinations.append(wordPermutationsList)
        currentWordNumber = currentWordNumber + 1

    return allWordCombinations


def getAllPossibleWordPermutationsRec(lettersList, wordPermutation, wordPermutationsList, totalPermutationsPossible, processedPermutations, currentWordNumber):
    if(len(lettersList) == 0):
        wordPermutationsList.append(list(wordPermutation))
        processedPermutations.append((processedPermutations.pop() + 1))
        printProgressBar(processedPermutations[0], totalPermutationsPossible, prefix=(
            "Loading Word " + str(currentWordNumber)), suffix="Complete", length=50, fill="#")
        return

    for letter in lettersList[0]:
        wordPermutation.append(letter)
        getAllPossibleWordPermutationsRec(
            lettersList[1:], wordPermutation, wordPermutationsList, totalPermutationsPossible, processedPermutations, currentWordNumber)
        wordPermutation.pop()


def getAllPossibleSentences(allPossibleWordPermutations):

    if (len(allPossibleWordPermutations) > 0):
        totalPermutationsPossible = 1

        for word in allPossibleWordPermutations:
            totalPermutationsPossible = totalPermutationsPossible * len(word)
    else:
        totalPermutationsPossible = 0

    processedPermutations = [0]

    sentencePermutation = deque()
    sentencePermutationsList = list()

    getAllPossibleSentencesRec(allPossibleWordPermutations, sentencePermutation,
                               sentencePermutationsList, totalPermutationsPossible, processedPermutations)

    return sentencePermutationsList


def getAllPossibleSentencesRec(allPossibleWordPermutations, sentencePermutation, sentencePermutationsList, totalPermutationsPossible, processedPermutations):
    if(len(allPossibleWordPermutations) == 0):
        sentencePermutationsList.append(list(sentencePermutation))

        processedPermutations.append((processedPermutations.pop() + 1))

        printProgressBar(processedPermutations[0], totalPermutationsPossible, prefix=(
            "Loading Sentences"), suffix="Complete", length=50, fill="#")
        return

    for wordPermutation in allPossibleWordPermutations[0]:
        sentencePermutation.append("".join(wordPermutation))
        getAllPossibleSentencesRec(
            allPossibleWordPermutations[1:], sentencePermutation, sentencePermutationsList, totalPermutationsPossible, processedPermutations)
        sentencePermutation.pop()


def getPossibleLettersForWordPermutationList(digitSequence):
    possibleLetters = list()
    for digit in digitSequence:
        possibleLetters.append(charsForNum(digit))
    return possibleLetters


def getNumberOfAllWordPermutations(digitSequence):
    if(len(digitSequence) > 0):
        numberOfPerutations = 1
        for digit in digitSequence:
            numberOfPerutations = numberOfPerutations * len(charsForNum(digit))
        return numberOfPerutations
    else:
        return 0


def charsForNum(number):
    switcher = {
        '2': ['A', 'B', 'C'],
        '3': ['D', 'E', 'F'],
        '4': ['G', 'H', 'I'],
        '5': ['J', 'K', 'L'],
        '6': ['M', 'N', 'O'],
        '7': ['P', 'Q', 'R', 'S'],
        '8': ['T', 'U', 'V'],
        '9': ['W', 'X', 'Y', 'Z']
    }
    return switcher.get(number)


def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
    # method from user Greenstick at https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 *
                                                     (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()
