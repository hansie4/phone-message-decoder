
def getMessageToEncode():
    validMessageRetrieved = False

    while (not validMessageRetrieved):
        rawMessage = input("Enter Message to Encode: ")
        if(isMessageToEncodeValid(rawMessage)):
            return rawMessage
        else:
            print(
                "The message you entered was invalid. The only characters should be letters(any case), '-', '_', and ' '.")


def isMessageToEncodeValid(message):
    for character in message:
        if(not(character.isalpha() or character == ' ' or character == '-' or character == '_')):
            return False
    return True


def encodeMessage(message):
    encodedMessage = ""
    for character in message:
        encodedMessage = encodedMessage + encodeCharacter(character.upper())
    return encodedMessage


def encodeCharacter(character):
    switcher = {
        'A': '2',
        'B': '2',
        'C': '2',
        'D': '3',
        'E': '3',
        'F': '3',
        'G': '4',
        'H': '4',
        'I': '4',
        'J': '5',
        'K': '5',
        'L': '5',
        'M': '6',
        'N': '6',
        'O': '6',
        'P': '7',
        'Q': '7',
        'R': '7',
        'S': '7',
        'T': '8',
        'U': '8',
        'V': '8',
        'W': '9',
        'X': '9',
        'Y': '9',
        'Z': '9',
        ' ': '-',
        '-': '-',
        '_': '-',
    }
    return switcher.get(character)
