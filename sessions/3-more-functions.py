# Some homework questions I posed last time:
# Q: write a function that takes a list of integers and returns the smallest value in the list
# Q: write a function that takes a list of integers and returns a list of the absolute values of those integers

# summary:
#   python doesnt type-check (despite type specifying)
    #   could lead to error
    #   could lead to undesired behaviour
#   smallestValue
    #   input-checking
    #   conditionals
    #   not
#   unit-testing
    #   range()
#   python input/output aliasing
#   python function scope isn't limited to function

# unpredicted use leads to error (obvious)
def doSomething(l : list) -> int:
    for i in l: # this will cause error if you feed an int into this function
        return 1 

# unpredicted use leads to undeired behaviour (subtle) -- not an error
def computeProduct(l : list) -> list:
    product = [] 
    for i in l: 
        product.append(i * 5) 
    return product
 
def smallestValue(l : list) -> int:
    if (not listOfInts(l)):
        print("MyError: smallestValue() should take a list of ints")
        return

    smallest = l[0]
    for i in l:
        if i < smallest:
            smallest = i
    return smallest

def listOfInts(l : list) -> bool:
    if (type(l) != list):
        return False
    for i in l:
        if (type(i) != int):
            return False
    return True

def absoluteList(l : list) -> list:
    if (not listOfInts(l)):
        print("MyError: absoluteList() should take a list of ints")
        return
    absolutes = l # what about l.copy()
    for i in range(0, len(absolutes)):
        absolutes[i] = abs(absolutes[i])
    return absolutes

def absoluteList2(l : list) -> list:
    if (not listOfInts(l)):
        print("MyError: absoluteList() should take a list of ints")
        return
    absolutes = []
    for i in range(0, len(l)):
        absolutes.append(abs(l[i]))
    return absolutes

def someX():
    print(x) # this will work if x is defined outside scope of function


