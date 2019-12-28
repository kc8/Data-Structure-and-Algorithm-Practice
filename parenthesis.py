import stack

def parenthesisCheck(symbols):
    """
    Function to check if the given parentesis are balanced or not. 
    """
    s = stack.Stack()
    index = 0
    balanced = True
    while index < len(symbols): 
        symbol = symbols[index]
        if symbol in '{[(':
            s.push(symbol)
        else:
            if s.isEmpty(): balanced = False
            else: 
                top = s.pop()
                if not symbol_compare(top,symbol):
                    balanced = False
        index += 1 
    if balanced and s.isEmpty(): return True
    else: return False

def symbol_compare(open, close):
    opens = "[{("
    closes = "}])"
    return (open in opens) == (close in closes)

paren_string = '[{}[()]](())'
print(parenthesisCheck(paren_string))