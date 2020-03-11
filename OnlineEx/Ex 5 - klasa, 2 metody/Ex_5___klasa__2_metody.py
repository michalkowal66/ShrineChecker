class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getStr(self):
        self.s = input()

    def printStr(self):
        print(self.s.upper())

strObj = InputOutString()
strObj.getStr()
strObj.printStr()
