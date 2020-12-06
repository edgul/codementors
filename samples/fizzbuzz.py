
# write a function that takes an integer as input
# and outputs "fizz" if the number is a multiple of 3
#             "buzz" if the number is a multiple of 5
#             "fizzbuzz" if the number is multiple of 3 and 5
#             the number if neither

def fizzbuzz(x):
    result = ""
    if (x % 3 == 0):
        result += "fizz"
    if (x % 5 == 0):
        result += "buzz"
    if result == "":
        result = str(x)
    return result

def fizzbuzz2(x):
    result = ""
    if (x%3 == 0 and x%5 == 0):
        return "fizzbuzz"
    elif (x%3 == 0):
        return "fizz"
    elif (x%5 == 0):
        return "buzz"
    else:
        return str(x)


for i in range(25):
    print(fizzbuzz(i))
