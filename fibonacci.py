def fibonacci(fibIndex):
    #Invalid data types
    if(not isinstance(fibIndex, int)):
        raise Exception("Fibonacci expects an integer")
    
    if(fibIndex < 0):
        raise Exception("Fibonacci expects a positive integer")

    #Base cases
    if(fibIndex == 0):
        return 0

    if(fibIndex == 1):
        return 1

    #Cases >= 2
    prevPrev = 0
    prev = 1

    for i in range(2, fibIndex):
        tempPrev = prev
        prev = prevPrev + prev
        prevPrev = tempPrev

    return prev+prevPrev

def factorial(input):
    #Base cases
    if(input == 0):
        return 1

    if(input == 1):
        return 1

    #Cases >= 2
    runningTotal = input
    multiplier = input-1
    while(multiplier > 0):
        runningTotal = runningTotal * multiplier
        multiplier = multiplier - 1

    return runningTotal