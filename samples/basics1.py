
def main():
   
    ### expressions - these "evaluate" to something

    # primitives - aka basic datatypes
    120         # integer
    1.1         # float
    2+3j        # complex
    "hello"     # string 
    True        # bool
   
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
    # 1: 5 * 5 ** 2
    # 2: 5 + succ(5 + 6) / 3

    # functions
    print(5)    # output to screen
    float(5)    # conversions
    int(5.1)    
    round(5.6)  # rounding
    help(5)     # help!
    isinstance(5, int)

    # defining functions
    #   valueless functions (procedures)
    #   returning
    #   parameters
    # 1. successor()
    # 2. addTwo()

    # conditionals 
    #   if
    #   elif
    #   else
    # 1. write a function that returns true if the first string argument contains the second string argument 
    
    # collections
    [1, 2, 3, 4]       # list
    (1, 2)            # tuple
    {'a', 'b', 'c' }   # set
    {'a':1, 'b':2 }    # dict

    # List: print 1..10
    # Tuple: write function that returns line count and letter count of a given string

    # mutability

    # for loops

    # variables/assignment

    # basic formatting
    "Something is here" + str(5)

    # Errors:
    # TypeError     " " + 5
    # NameError     fsadfasd
    # ValueError    int("something")

    # Questions:
    # What is the difference between "something" and 'something'
    # What does this do?: " " + 5
    # What are results of round(-1.1) and int(-1.1)
    # If found in an expression what is diff between (1,1) and f(1,1)
    # What does this do?: x = print(5)

    # Problems:
    # User Input: Write a program that takes a number from a user and prints "The number was: <the_number>"
    # Conversion: Write a program that takes two numbers from a user and prints the sum of the two numbers
    # Conditionals: Fizzbuzz
    # Sets: Given two lists of ints return a list of the shared ints
    # Dict: Count the number of each letter in a given string - print each count

    
    
main()
