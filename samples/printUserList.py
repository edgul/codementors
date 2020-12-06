
# takes no input
# asks user for a set of numbers
# prints them all after user says done
def printUserList():
    l = []
    x = input()
    while x != 'done':
        l.append(x)
        x = input()
    print(l)

printUserList()


