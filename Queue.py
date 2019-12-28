class Queue:
    def __init__(self):
        """
        Create an empy queue. 
        """
        self.items = []
    
    def isEmpty(self):
        """
        Checks to see if the queue is empty. Returns boolean
        """
        return self.items == []
    
    def enqueue(self, item):
        """
            Qeues an element in the queue at the rear
        """
        # adds the item to the first position so we can use Python list functions. 
        # This means that position 0 in the list is the read of the queue. 
        self.items.insert(0, item)
    
    def dequeue(self):
        """
            Removes an element from the front of the queue.
        """
        # finds and removes the item in the list using list method
        return self.items.pop()
    
    def size(self):
        """
            Return the size of the elements in the queue
        """
        return len(self.items)
    
    def peek(self):
        """
            See the element at the front of the queue
        """
        return self.items[len(self.items)- 1]

