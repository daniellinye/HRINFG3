
class SQLInsterter:
    def __init__(self):
        self.list = []
        self.table = ""
        self.values = []

    def printlist(self):
        for i in range (0,len(self.values)):
            for items in self.list:
                print("INSTERT INTO {} ".format(self.table) + "({})".format(self.values))

