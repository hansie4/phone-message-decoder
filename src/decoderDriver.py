from decoderHelper import *

message = input("Enter the message to decode: ")

if(isMessageValid(message) != True):
    print("Message invalid. Exiting program.")
    exit()

allPossibleStrings = getAllStrings(message)

printStringsList(allPossibleStrings)
