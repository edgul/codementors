# Some homework questions I posed last time:
# Q: write a function that takes a list of integers and returns the smallest value in the list

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


# input: list of ints input; returns list multiplied by 5
# this function demonstrates how feeding incorrect types into python function can cause unexpected behaviour (without causing error)
def computeProduct(l):
    if (type(l) != list):
        print("MyWarning: This is not a list")
        return
        #raise ValueError("MyWarning: The list is empty") # might be more appropriate to cause error message instead of ouputting and returning
    product = []
    for integer in l:
        product.append(integer * 5)
    return product

# our own test to check input types
# we can use this to verify the inputs to our functions match the function spec
def listOfInts(l : list) -> bool:
    if (type(l) != list):
        print("MyWarning: This is not a list")
        return False
    if (len(l) == 0):
        print("MyWarning: List is empty")
        return False
    for i in l:
        if type(i) != int:
            return False
    return True

# unit testing
def testListOfInts():
    l1 = ["1"]
    l2 = []
    l3 = [1,2,3,4,5]
    l4 = [1,2,3,4, "6"]
    print(listOfInts(l1))
    print(listOfInts(l2))
    print(listOfInts(l3))
    print(listOfInts(l4))
    print(listOfInts(bool))
    print(listOfInts(True))

# write a function that takes a list of integers
# and returns the value in the list that is the smallest value
def smallestValue(someList : list) -> int:
    if not listOfInts(someList):
        print("MyWarning: The list is not a list of ints")
        return
        #raise ValueError("MyWarning: The list is empty")
    smallestSoFar = someList[0]
    for i in someList:
        if (i < smallestSoFar):
            smallestSoFar = i
    return smallestSoFar

# unit testing
def testSmallestValue():
    l1 = [1,2,3]
    l2 = []
    l3 = [-1, -10, 30]
    l4 = ["text"]
    l5 = [7, 23, -100, 0]
    l6 = [999999]
    print("Should return 1 " + str(l1))
    print(smallestValue(l1))
    print()
    print(smallestValue(l2))
    print()
    print(smallestValue(l3))
    print()
    print(smallestValue(l4))
    print()
    print(smallestValue(l5))
    print()



