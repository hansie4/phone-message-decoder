from decoderHelper import *


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

        printPermutationsToFile(allPossibleSentences, outputFileName)

        # printPermutationsToFile(
        # allPossibleWordPermutations, outputFileName)

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
    print("2: Get all permutations with a valid english word **NOT YET IMPLEMENTED**")
    print("3: Get all permutations with only valid english words **NOT YET IMPLEMENTED**")
    print("4: Go back")

    while (not menuSelected):
        menuSelection = input("Enter 1, 2, 3, or 4: ")
        if((menuSelection == '1') or (menuSelection == '2') or (menuSelection == '3') or (menuSelection == '4')):
            menuSelected = True

    return menuSelection


def printPermutationsToFile(allPermutations, fileName):
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
