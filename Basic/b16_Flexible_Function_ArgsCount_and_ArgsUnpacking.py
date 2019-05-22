# this function takes however much aguments you give
def Multiply_args(*args):
    total = 1
    for i in args:
        total *= i
    return total

# this is the normal way of calling the function and feeding the arguments
myVal0 = Multiply_args(4, 5, 3)
print(myVal0)

myVal1 = Multiply_args(3, 9, 4, 7, 3, 4, 5, 3)
print(myVal1)

# if you had the args in a list
myArgs = [1, 5, 9, 3, 9]

myVal2  = Multiply_args(myArgs[0],myArgs[1],myArgs[2],myArgs[3],myArgs[4])

# a simpler way to throw in all the args would be args unpacking
myVal3 = Multiply_args(*myArgs)

# both of them does the exact same thing but the one that uses args unpacking is way simpler and more readable

print(myVal2)
print(myVal3)