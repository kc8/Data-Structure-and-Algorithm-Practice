import time


def sumofN(n):
    """
    Computes the first n integers. Using recursion
        BigO notes: this is T(N) = 1 + n where n is the number of times theSum is calculated
    """

    theSum = 0
    for i in range(1, n+1):
        theSum += i
    return theSum

print(sumofN(10))  

def sumofNBenchmark(n):
    """Computes the first n integers. Using recursion
        Returns the time it took to execute
    """
    start = time.time()

    theSum = 0
    for i in range(1, n+1):
        theSum += i
    
    end = time.time()
    
    return theSum,end-start #return the amount of time it took to execute the program

#sumofints = sumofNBenchmark(100000000000000000000)
#print("The sum of the integers are: ", sumofints[0], " and thetime required: ", sumofints[1])  

def sumofN3(n):
    start = time.time()
    return (n*(n+1))/2, start-time.time() 

sumofints = sumofN3(100000000000000000000)
print("The sum of the integers are: ", sumofints[0], " and thetime required: ", sumofints[1])  
