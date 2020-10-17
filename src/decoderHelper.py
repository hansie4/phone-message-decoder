from collections import deque
from anytree import Node, RenderTree


def isMessageValid(message):

    if(message):
        for character in message:
            if((character != '-') and (character != '2') and (character != '3') and (character != '4') and (character != '5') and (character != '6') and (character != '7') and (character != '8') and (character != '9')):
                return False

        return True
    else:
        return False


def getAllStrings(message):

    stringTree = getStringTree(message, "Tree")

    printStringTree(stringTree)

    path = deque()
    stringList = list()

    for node in stringTree.children:
        getAllStringsRec(node, path, stringList)

    return stringList


def getAllStringsRec(node, path, stringList):
    if node is None:
        return

    path.append(node.name)

    if (node.children == ()):
        stringList.append(list(path))

    for childNode in node.children:
        getAllStringsRec(childNode, path, stringList)

    path.pop()


def findAllStringsWithRealWords():
    pass


def charsForNum(number):
    switcher = {
        '2': ['A', 'B', 'C'],
        '3': ['D', 'E', 'F'],
        '4': ['G', 'H', 'I'],
        '5': ['J', 'K', 'L'],
        '6': ['M', 'N', 'O'],
        '7': ['P', 'Q', 'R', 'S'],
        '8': ['T', 'U', 'V'],
        '9': ['W', 'X', 'Y', 'Z'],
        '-': ['-']
    }
    return switcher.get(number)


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


def printStringsList(stringList):
    index = 1
    for string in stringList:
        print(str(index) + ":\t" + "".join(string))
        index = index + 1


def printStringTree(stringTree):
    for pre, fill, node in RenderTree(stringTree):
        print("%s%s" % (pre, node.name))
