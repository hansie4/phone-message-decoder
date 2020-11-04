from decoderHelper import *
from dictionaryHelper import *


def decodePhoneKeypadMessage(outputFileName):

    decoding = True

    menuSelection = getDecodingMenuSelection()

    if(menuSelection == '1'):
        # Get all possible permutations
        rawMessage = getValidMessageToDecode()
        allPossibleWordPermutations = getAllPossibleWordPermutations(
            rawMessage)

        allPossibleSentences = getAllPossibleSentences(
            allPossibleWordPermutations)

        writePermutationsToFile(allPossibleSentences, outputFileName)

        input("\nPress Enter to Continue.")
    elif (menuSelection == '2'):
        # Get all permutations with a valid english word
        rawMessage = getValidMessageToDecode()
        allPossibleWordPermutations = getAllPossibleWordPermutations(
            rawMessage)

        wordDict = loadWordDict("dictionaries/english_words_dictionary.txt")

        allPossibleSentences = getAllPossibleSentences(
            allPossibleWordPermutations)

        validSentences = list()

        iteration = 0
        total = len(allPossibleSentences)

        for possibleSentence in allPossibleSentences:
            for word in possibleSentence:
                if wordDict.isWordInDict(word):
                    validSentences.append(possibleSentence)
            iteration = iteration + 1
            printProgressBar(iteration, total, prefix=(
                "Loading Sentences"), suffix="Complete", length=50, fill="#")

        writePermutationsToFile(validSentences, outputFileName)

        input("\nPress Enter to Continue.")
    elif (menuSelection == '3'):
        # Get all permutations with only valid english words
        rawMessage = getValidMessageToDecode()

        allPossibleWordPermutations = getAllPossibleWordPermutations(
            rawMessage)

        wordDict = loadWordDict("dictionaries/english_words_dictionary.txt")

        validWordsLists = list()

        for wordPermutationList in allPossibleWordPermutations:
            validWords = list()
            for currentWordPermutation in wordPermutationList:
                if (wordDict.isWordInDict("".join(currentWordPermutation))):
                    validWords.append(currentWordPermutation)
            validWordsLists.append(validWords)

        allPossibleSentences = getAllPossibleSentences(validWordsLists)

        writePermutationsToFile(allPossibleSentences, outputFileName)

        input("\nPress Enter to Continue.")
    else:
        decoding = False


def getDecodingMenuSelection():
    menuSelected = False
    menuSelection = '-1'

    print("\tDECODING MENU:")
    print("1: Get all possible permutations")
    print("2: Get all permutations with a valid english word")
    print("3: Get all permutations with only valid english words")
    print("4: Go back")

    while (not menuSelected):
        menuSelection = input("Enter 1, 2, 3, or 4: ")
        if((menuSelection == '1') or (menuSelection == '2') or (menuSelection == '3') or (menuSelection == '4')):
            menuSelected = True

    return menuSelection


def writePermutationsToFile(allPermutations, fileName):
    file = open(fileName, "w")

    totalPermutationsPossible = len(allPermutations)
    processedPermutations = 0

    currentPermutationNumber = 1
    for permutation in allPermutations:
        file.write(str(currentPermutationNumber) +
                   ": " + "-".join(permutation) + "\n")

        processedPermutations = processedPermutations + 1

        printProgressBar(processedPermutations, totalPermutationsPossible, prefix=(
            "Writing Sentences"), suffix="Complete", length=50, fill="#")

        currentPermutationNumber = currentPermutationNumber + 1

    print(f"Possible sentences can be found in {fileName}")

    file.close()
