import stack

def operate(equation):
    """
    @param takes a string equation like (A+B)*C. Does not account for spaces
    """
    prec = {
        '*' : 3, 
        '/' : 3,
        '+' : 2,
        '-' : 2,
        '(' : 1,
    }
    output_list = []
    operators = "+-*/()"
    operand_tokens = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    operator_stack = stack.Stack()
    equation_tokens = [i for i in equation.split()[0]]

    for i in equation_tokens:
        if i in operand_tokens:
            output_list.append(i)
        elif i == "(" :
            operator_stack.push(i)
        elif i == ")": #what if the stack is empty? 
            if operator_stack.isEmpty():
                return "Equation is not balanced"
            else:
                top_token = operator_stack.pop()
                while top_token != '(':
                    output_list.append(top_token)
                    top_token = operator_stack.pop()
        else: 
            while (not operator_stack.isEmpty()) and \
                (prec[operator_stack.peek()] >= prec[i]):
                output_list.append(operator_stack.pop())
            operator_stack.push(i)
    while not operator_stack.isEmpty():
        output_list.append(operator_stack.pop())
    return " ".join(output_list)
                
    #if token is operator push to stack and remove higher precdant operators on stack 
        


print(operate("(A+B)*(C+B)"))