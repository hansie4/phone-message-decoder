from decoderHelper import *


def decodePhoneKeypadMessage():

    rawMessage = getValidMessageToDecode()

    allWordPermutations = getAllWordPermutations(rawMessage)

    printPermutationsToFile(allWordPermutations, "word_possibilities.txt")


def printPermutationsToFile(allWordPermutations, fileName):
    file = open(fileName, "w")

    currentWordNumber = 1
    for wordPermutations in allWordPermutations:

        totalPermutationsPossible = len(wordPermutations)
        processedPermutations = 0

        file.write(f"\t\tWORD {currentWordNumber}\n")

        currentWordPermutationNumber = 1
        for combination in wordPermutations:
            file.write(str(currentWordPermutationNumber) +
                       ":" + "".join(combination) + "\n")

            processedPermutations = processedPermutations + 1

            printProgressBar(processedPermutations, totalPermutationsPossible, prefix=(
                "Writing Word " + str(currentWordNumber)), suffix="Complete", length=50)

            currentWordPermutationNumber = currentWordPermutationNumber + 1
        currentWordNumber = currentWordNumber + 1

    print(f"Possible Words can be found in {fileName}")

    file.close()
