from collections import deque
from anytree import Node, RenderTree


def getValidMessageToDecode():
    validMessageRetrieved = False

    while (not validMessageRetrieved):
        rawMessage = input("Enter Message to Decode: ")
        if(isMessageToDecodeValid(rawMessage)):
            return rawMessage
        else:
            print(
                "The message you entered was invalid. The only characters should be digits 2-9 and '-'.")


def isMessageToDecodeValid(message):

    if(message):
        for character in message:
            if((character != '-') and (character != '2') and (character != '3') and (character != '4') and (character != '5') and (character != '6') and (character != '7') and (character != '8') and (character != '9')):
                return False

        return True
    else:
        return False


def getPartitionedMessage(message):
    return message.split("-")


def getAllWordPermutations(message):

    partitionedMessage = getPartitionedMessage(message)

    wordTrees = list()

    allWordCombinations = list()

    currentWordNumber = 1
    for digitSequence in partitionedMessage:

        wordTree = getStringTree(
            digitSequence, "Word " + str(currentWordNumber))
        wordTrees.append(wordTree)

        path = deque()
        wordPermutationList = list()

        for node in wordTree.children:
            getAllWordPermutationsRec(node, path, wordPermutationList)

        allWordCombinations.append(wordPermutationList)

        currentWordNumber = currentWordNumber + 1

    return allWordCombinations


def getAllWordPermutationsRec(node, path, wordPermutationList):
    if node is None:
        return

    path.append(node.name)

    if (node.children == ()):
        wordPermutationList.append(list(path))

    for childNode in node.children:
        getAllWordPermutationsRec(
            childNode, path, wordPermutationList)

    path.pop()


def getStringTree(message, rootNodeName):
    return Node(rootNodeName, children=getStringTreeRec(message))


def getStringTreeRec(restOfMessage):
    nodes = []
    if(len(restOfMessage) == 1):
        for char in charsForNum(restOfMessage[0]):
            nodes.append(Node(name=char))
        return nodes
    else:
        for char in charsForNum(restOfMessage[0]):
            nodes.append(
                Node(name=char, children=getStringTreeRec(restOfMessage[1:])))
        return nodes


def printStringTree(stringTree):
    for pre, fill, node in RenderTree(stringTree):
        print("%s%s" % (pre, node.name))


def printAllWordPermutations(allWordPermutations):
    currentWord = 1
    for wordPermutations in allWordPermutations:
        print("\t\tWORD " + str(currentWord) +
              " (" + str(len(wordPermutations)) + ")")
        for combination in wordPermutations:
            print(combination)
        currentWord = currentWord + 1


def getNumberOfAllPermutations(digitSequence):
    if(len(digitSequence) > 0):
        numberOfPerutations = 1
        for digit in digitSequence:
            numberOfPerutations = numberOfPerutations * len(charsForNum(digit))
        return numberOfPerutations
    else:
        return 0


def charsForNum(number):
    switcher = {
        '2': ['A', 'B', 'C'],
        '3': ['D', 'E', 'F'],
        '4': ['G', 'H', 'I'],
        '5': ['J', 'K', 'L'],
        '6': ['M', 'N', 'O'],
        '7': ['P', 'Q', 'R', 'S'],
        '8': ['T', 'U', 'V'],
        '9': ['W', 'X', 'Y', 'Z']
    }
    return switcher.get(number)


def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
    # method from https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 *
                                                     (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()
