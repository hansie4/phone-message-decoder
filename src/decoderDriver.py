from decoderHelper import *


def decodePhoneKeypadMessage(outputFileName):

    decoding = True

    menuSelection = getDecodingMenuSelection()

    if(menuSelection == '1'):
        # Get all possible permutations
        rawMessage = getValidMessageToDecode()
        allPossibleWordPermutations = getAllPossibleWordPermutations(
            rawMessage)

        printPermutationsToFile(
            allPossibleWordPermutations, outputFileName)

        input("\nPress Enter to Continue.")
    elif (menuSelection == '2'):
        # Get all permutations with a valid english word
        rawMessage = getValidMessageToDecode()
        input("\nPress Enter to Continue.")
    elif (menuSelection == '3'):
        # Get all permutations with only valid english words
        rawMessage = getValidMessageToDecode()
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
                "Writing Word " + str(currentWordNumber)), suffix="Complete", length=50, fill="#")

            currentWordPermutationNumber = currentWordPermutationNumber + 1
        currentWordNumber = currentWordNumber + 1

    print(f"Possible Words can be found in {fileName}")

    file.close()
