from decoderHelper import *


def decodePhoneKeypadMessage():

    rawMessage = getValidMessageToDecode()

    allWordPermutations = getAllWordPermutations(rawMessage)

    printAllWordPermutations(allWordPermutations)
