# basic2.py

# review from last time:
#  * basic functions
#  * comments
#  * procedural nature of programming (executing one line at a time)
#  * help(...) function

# new topics:
# mutability
# aliasing vs copying
# lists
# * indexing
# * slicing
# * modifying
# more functions
# * scope (indentation)
# * defining vs calling
# * parameters/arguments
#   -> list as argument
#   -> specifying parameter type
#   -> "error" message to prevent function misuse with incorrect type
# functions taking lists
# conditionals
# * if
# * else
# * elif
# for loop (only iterating through existing list and strings - still a lot to discuss here)

# some homework to practice:
# Q: write a function that takes an integer and prints from 0 to that integer
# Q: write a function that takes two integers (start and end) that prints intgers between those values
# Q: write a function that takes a list of integers and returns the smallest value in the list
# Q: write a function that takes a list of integers and returns the average (mean) of the list
# Q: write a function that takes a list of integers and returns a list of the absolute values of those integers
    
# print all values in the list
def printList(someList : list):
    if (type(someList) != list):
        print("Error: printList should take a list")
        return
    # processing
    for i in someList:
        print(i)

# returns incremented value passed
def successor(n : int) -> int:
    return n + 1

def someConditional():
    strawberry = "stawbey"
    if (strawberry.count("z") > 1):
        print("Yes there is at least one 'r'")
    elif (strawberry.count('r') > 1):
        print("No z, but there are rs")
    else:
        print("Nope, no 'r's here")
   
    
   # starting point to program
def main():
    print(successor(5))
    someTestFunction()
    
main()


