from decoderDriver import *
from encoderDriver import *

OUTPUT_FILE_NAME = "ouput.txt"


def main():
    programRunning = True

    print("This program encodes and decodes messages in the format of numbers corresponding to letters on a phone keypad seperated by a '-'. (ex. 6233-29-4267 = MADE-BY-HANS). Due to ambiguity in what character the number corresponds to the program outputs all possible combinations of letters based on the input when decoding.")

    while programRunning:
        menuSelection = getMenuSelection()

        if(menuSelection == '1'):
            decodePhoneKeypadMessage(OUTPUT_FILE_NAME)
        elif (menuSelection == '2'):
            encodePhoneKeypadMessage()
            input("\nPress Enter to Continue.")
        else:
            programRunning = False

    exitProgram()


def getMenuSelection():
    menuSelected = False
    menuSelection = '-1'

    print("\tMAIN MENU:")
    print("1: Decode A Message")
    print("2: Encode A Message")
    print("3: Exit")

    while (not menuSelected):
        menuSelection = input("Enter 1, 2, or 3: ")
        if((menuSelection == '1') or (menuSelection == '2') or (menuSelection == '3')):
            menuSelected = True

    return menuSelection


def exitProgram():
    print("Exiting program.")
    exit()


if __name__ == "__main__":
    main()
