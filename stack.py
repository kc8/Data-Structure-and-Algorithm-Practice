class Stack: #create a stack class

    def __init__(self):
        self.items = []   #use a more primite data struct to create our stack. 
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        """
        Returns the top item of the stack
        """
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return self.items
        
    
#s = Stack()

#print(s.isEmpty())
#s.push(4)
#s.push(5)
#print(s.peek())
#print(s.size())
#print(s.isEmpty())


#Challenege: Write a function revstring(mystr) that uses a stack to reverse the characters in a string.
#https://runestone.academy/runestone/books/published/pythonds/BasicDS/ImplementingaStackinPython.html

