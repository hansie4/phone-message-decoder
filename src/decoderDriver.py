from decoderHelper import *


def main():
    message = input("Enter the message to decode: ")

    if(isMessageValid(message) != True):
        print("Message invalid. Exiting program.")
        exit()

    allPossibleStrings = getAllStrings(message)

    printStringsList(allPossibleStrings)


if __name__ == "__main__":
    main()
