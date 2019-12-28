#Uses a stack to check that a word is spelled the same way both back and forth for example
#madam, toot, and radar 

import Deque

def palchecker(word):
    deque = Deque.Deque()

    for i in word: 
        deque.addRear(i)
    
    stillEqual = True

    while deque.size() > 1 and stillEqual: 
        first = deque.removeFront()
        last = deque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual

print(palchecker("radar"))
print(palchecker("nothing"))