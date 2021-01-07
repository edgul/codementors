
# Q: write a function that takes a list of integers and returns a list of the absolute values of those integers
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

