

 # "like" x + y
 # make me a function that returns the sum of two numbers with the name "add"
def add(a,b): # signature
    return a + b


def addMany(a,b,c,d,e,f):
    return a + b + c + d + e + f

def addMany2(a,b,c):
    temp = a + b
    return temp + c

def addMany3(a,b,c):
    temp = a + b
    temp += c
    return temp
# function that counts a given letter in a string
# inputs: a string
#         a letter
# output: the number of times we see the letter in that string
def countLetters(someStr,letter):
    return someStr.count(letter)

def hello():
    x = "hello"
    y = 1
    z = 5


countLetters("somestring", "a")
print(someStr)


# Summary - Dec 6, 2020:
# * expressions/values
# * assignment
# * used built-in functions (min,max, print, help)
# * created our own functions (add,countLetters)
#     procedures (don't return a value)
#     expression-functions (returns a value)
#     scope
# * used objects (string)
# * created time class (just barely -- don't spend too much time here yet)

# Some questions
# 1. Write your own max function without using the built-in verion (2 int inputs and returns the lower of the two)
# 2. So the same for min function
# 3. Write a function that takes a string and a letter as a delimiter. It should print each substring as its own line:
# 	IE: f("hello", "e") would print the lines "h" and "llo"

