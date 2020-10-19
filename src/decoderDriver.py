from decoderHelper import *


def main():
    print("This program takes a message in the form of the numbers that correspond to numbers on a phone's keypad (words seperated by '-') and decodes possible meanings.")
    rawMessage = input("Enter the message to decode: ")

    if(isMessageValid(rawMessage) != True):
        print("Message invalid. Exiting program.")
        exit()

    rawMessagePartitioned = getPartitionedMessage(rawMessage)

    possibleWords = list()

    for word in rawMessagePartitioned:
        possibleWords.append(getAllStrings(word))

    # DEBUGGING
    # for words in possibleWords:
    #    print("------------")
    #    for word in words:
    #        print("".join(word))
    # print("------------")


if __name__ == "__main__":
    main()
