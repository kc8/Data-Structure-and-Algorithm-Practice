import random

def find_min(range_length): 
    """
        Returns the minimum value in the given range
        The first function should compare each number to every other number on the list n^2
    """
    rand_range = []
    for i  in range(range_length):
        rand_range.append(random.randrange(0, 10000, 1))
    min_num = 10000 #1346
    print(rand_range)
    for i in rand_range: #n 1346
        for x in rand_range: #n 1346
             if i <= x: 
               if min_num >= x:
                   min_num = x
    return min_num
    


def find_min_n(range_length):
    """
        Creates a random list of range_legnth and returns the smallest int
        The second function should be linear. n 
    """
    #find_minimum_number built in function
    rand_range = []
    for i  in range(range_length):
        rand_range.append(random.randrange(0, 10000, 1))
    min_num =  rand_range[0]
    print(rand_range)
    for i in rand_range: #n 1346
        if min_num >= i:
            min_num = i
    return min_num


range_length = 1000
print(find_min_n(range_length))
print(find_min(range_length))
