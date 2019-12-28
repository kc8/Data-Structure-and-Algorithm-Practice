
class Deque:

    def __init__(self):
        self.list = [] #create an empty list in which we can use for our data structure.
        
    def addFront(self, item):
        self.list.insert(0, item)    
    
    def addRear(self, item):
        self.list.append(item)

    def removeFront(self):
        return self.list.pop(0)

    def removeRear(self):
        return self.list.pop()

    def isEmpty(self):
        return self.list == []

    def size(self):
        return len(self.list)