class Node:
    def __init__(self, symbol = None):
        self.left = None
        self.right = None
        self.symbol = symbol

    def getNodeLeft(self):
        if not self.left:
            self.left = Node()
        return self.left

    def getNodeRight(self):
        if not self.right:
            self.right = Node()
        return self.right

    def getSymbol(self):
        return self.symbol

    def setSymbol(self, symbol):
        self.symbol = symbol

    def getNode(self, code):
        if code == 0:
            return self.getNodeLeft()
        return self.getNodeRight()

    def initTree(self, codeword, symbol):
        if len(codeword) == 0:
            return self.setSymbol(symbol)
        code = codeword.pop(0)
        self.getNode(code).initTree(codeword, symbol)

class PrefixCodeTree:
    def __init__(self):
        self.codeTree = Node()

    def insert(self, codeword, symbol):
        self.codeTree.initTree(codeword, symbol)

    def decode(self, encodedData, datalen):
        bits = "{:08b}".format(int (encodedData.hex(), 16) )[:datalen]
        return self._decode(bits)

    def _decode(self, bits):
        currentNode = self.codeTree
        decoded = ''
        for b in bits:
            currentNode = currentNode.getNode(int(b))
            if currentNode.getSymbol():
                decoded += currentNode.getSymbol()
                currentNode = self.codeTree
        return decoded
        
# codeTree = PrefixCodeTree()
# codebook = {
#     'x1': [0],
#     'x2': [1, 0, 0],
#     'x3': [1, 0, 1],
#     'x4': [1, 1]
# }

# for symbol in codebook:
#     codeTree.insert(codebook[symbol], symbol)
# message = codeTree.decode(b'\xd2\x9f\x20', 21)
# print(message)