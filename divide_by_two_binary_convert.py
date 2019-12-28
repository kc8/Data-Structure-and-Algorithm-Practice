#Alg: 
#1. Start with in greater than 0 
#3. Itterate and continue to divide the numerb by two
#3.1 first itt tells us whether odd or even
#

import stack

def divideBy2(dec_number):
    rem_stack  = stack.Stack()

    while dec_number > 0: 
        rem = dec_number % 2
        rem_stack.push(rem)
        dec_number= dec_number // 2
    
    bin_string = ""

    while not rem_stack.isEmpty():
        bin_string += str(rem_stack.pop())
    return bin_string

def baseconverter(num, base):
    digits = "0123456789ABCDEF"
    rem_stack = stack.Stack()

    while num > 0:
        rem = num % base
        rem_stack.push(rem)
        num = num // base
    
    converted_num = ""
    while not rem_stack.isEmpty():
        converted_num = converted_num + digits[rem_stack.pop()]
    return converted_num

print(divideBy2(25))
print(baseconverter(26, 26))
 
