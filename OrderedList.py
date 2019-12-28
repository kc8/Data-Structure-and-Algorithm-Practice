import Node as Node

class OrderedList:

    def __init__(self):
        self.head = None
        self.tail = None
        #self.size = 0 #future size function, having troulbe with pylint? 
    
    def isEmpty(self):
        return self.head == None
    
    def size(self):
        current = self.head
        count = 0

        while current != None: 
            count += 1
            current = current.getNext()
        return count

    def add(self, item):
        '''
        '''
        previous = None
        current = self.head
        added = False
        temp = Node.Node(item)

        while current != None and not added:
            if current.getData() > item:
                added = True 
            else:
                previous = current 
                current = current.getNext()
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

 
    def search(self, item):
        # Can stop searching once item is larger then what we are looking at
        current = self.head
        found = False
        proceed = True
        while current != None and not found and proceed:
            if current.getData() > item:
                proceed = False
            elif current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found 
    
    def display(self):
        #fix this to not use a list. To-Do: Can we make this iterable instead of returning built in list?
        done = self.size()
        templist = []
        count = 0
        current = self.head
        while done != count:
            templist.append(current.getData())
            current = current.getNext()
            count += 1
        return templist

mylist = OrderedList()

mylist.add(5)
mylist.add(6)
print(mylist.size())
mylist.add(7)
print(mylist.size())
print(mylist.display())

