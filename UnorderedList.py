import Node as Node

class UnorderedList:

    def __init__(self):
        self.head = None
        self.tail = None #init this value to something

    def isEmpty(self):
        return self.head == None
    
    def add(self, item):
        '''
            Items are added in a stack fasion
            The head of the list becomes the new node that is added. 
        '''
        temp = Node.Node(item)
        temp.setNext(self.head)
        self.head = temp 
        # Sets the tail to our grounded node, or the end, which will be our first node. 
        if temp.getNext() == None: 
            self.tail = temp
    
    def getTail(self):
        return self.tail

    def size(self):
        current = self.head
        count = 0

        while current != None: 
            count += 1
            current = current.getNext()
        return count
    
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found: 
            if item == current.getData():
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        """
            Removes an item from the linked list.
            To-do: Error handling if item is not found. Last item in the linked list? 
        """
        current = self.head
        found = False
        previous = None
        while not found: 
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext() #if previous is the first item, change the head
        else: 
            previous.setNext(current.getNext()) #Remove the node 
    
    def index(self):
        return None
    
    def insert(self, item): 
        return None
    
    def pop(self, item):
        return None

    def appendOne(self,item):
        """
            Append to the end of the list. This is an o(1) operation 
            This method will override anything done with append() function or the n^2 one. 
        """
        # set current node to have head == null or ground.
        temp = Node.Node(item)
        print(self.tail)
        self.tail.setNext(temp)
        self.tail = temp
        print(self.tail)
        temp.setNext(None) #ground the new node. 
   
    def append(self, item): 
        """
            Append item to the end of the list
            We can make this an O(1) operation. See AppendOne function
            to-do: 
                What if the list is empty? Create a new linked list with item as head

        """
        current = self.head
        found = False
        previous = None
        while not found:
            if current.getNext() == None:
                # cahnge  prvious node to have new head
                # set current node to have head == null or ground.
                temp = Node.Node(item)
                temp.setNext(None)
                current.setNext(temp)
                found = True
                #print(previous.getNext())
                #print(current.getNext())
            else:
                previous = current
                current = current.getNext()
    
    def display(self):
        #fix this to not use a list 
        done = self.size()
        templist = []
        count = 0
        current = self.head
        while done != count:
            templist.append(current.getData())
            current = current.getNext()
            count += 1
        return templist

    
mylist = UnorderedList()   

mylist.add(45)
mylist.add(56)



#mylist.append(5)
#mylist.append(6)
mylist.add(89)
mylist.appendOne(7)
mylist.appendOne(8)
mylist.add(78)
mylist.appendOne(56)
print(mylist.display())
