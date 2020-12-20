
def main():
   
    ### expressions - these "evaluate" to something

    # primitives - aka basic datatypes
    120         # integer
    1.1         # float
    2+3j        # complex
    "hello"     # string 
    True        # bool
    # Q: What is the difference between "something" and 'something'
    # What does this do?: " " + 5
   
    # complex expressions - built up of expressions with operators
    1 + 1                                   # arithmetic operators
    10 - 5
    5**2
    "a few " + "concatenated " + "strings"  # concatenated strings
    True and False                          # bool comp
    True or True                             
    not True
    5 == 5                                  # comparison operator
    5 != 4

    # order of evaluation 
    #   aka operator precedence
    #   overriding precedence
    # Q: 2 * 3 * 4 * 5
    # Q: 1 + 2 + 3 * 4
    # Q: 5 * 5 ** 2
    # Q: 5 + abs(5 + 6) / 3

    # Errors:
    # TypeError     " " + 5
    # NameError     fsadfasd
    # ValueError    int("something")


    #### built-in functions
    print(5)    # output to screen
    input()     # input from user
    # Q: User Input: Write a program that takes a number from a user and prints "The number was: <the_number>"

    float(5)    # conversions
    int(5.1)    
    round(5.6)  # rounding
    help(5)     # help!
    isinstance(5, int)
    range(1,10)
    # Q: What are results of round(-1.1) and int(-1.1)
    # Q: What does this do?: x = print(5)


    ##### defining functions
    #   valueless functions (procedures)
    #   returning
    #   parameters
    #   scope
    # Ex: five()
    # Ex: successor()
    # Ex: addTwo()
    # Q: write function countLetter(someStr, char) -> int
    # Q: write function max(x,y) (without using max)
    # Q: write function min(x,y) (without using min)


    ##### conditionals 
    #   if
    #   elif
    #   else
    # Q: write function printEvenOrOdd(n)
    # Q: write function belowIsOrAboveTen(n)
   


    # collections
    [1, 2, 3, 4]       # list
    (1, 2)            # tuple
    {'a', 'b', 'c' }   # set
    {'a':1, 'b':2 }    # dict

    # List: 
    l = []
    l = list()
    
    # for loops
    for i in range(10):
        print(i)

    listOfStrings = ["hello", "my", "name", "is", "ed"]
    for text in listOfStrings:
        print(text)
    # Q: print numbers one through n 
    # Q: find the largest value in the list
    # Q: find the smallest value in the list
    # Q: return a list of only the negative numbers in given list
    # Q: return a list of absolute values of the given list
    # Q: print only even numbers from 0 up to n
    # Q: write a function that takes an integer and sums all numbers from 1 to that number

    # Mutability
    # str vs list
    # passing by value vs passing by reference
    
    # Tuple: write function that returns line count and letter count of a given string
    # Sets: Given two lists of ints return a list of the shared ints

    # Problems:
    # Conditionals: Fizzbuzz
    # Dict: Count the number of each letter in a given string - print each count

    
    
main()
