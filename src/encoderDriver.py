from encoderHelper import *


def encodePhoneKeypadMessage():
    messageToEncode = getMessageToEncode()

    encodedMessage = encodeMessage(messageToEncode)

    print("Encoding of your message: " + encodedMessage)
