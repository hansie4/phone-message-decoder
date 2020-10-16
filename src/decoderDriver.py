from decoderHelper import *

message = input("Enter the message to decode: ")

allPossibleStrings = []

if(isMessageValid() != True):
    print("Message invalid. Exiting program.")
    exit()
