
#Lambda 
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, 
# but can only have one expression.
# Syntax
# lambda arguments : expression


x = lambda a : a + 10
print(x(4))

x = lambda a, b : a * b
print(x(5,5))


x = 5#int(input("Ingresa 3 números: "))
y = 3#int(input("Ingresa 2 números: "))
z = 4#int(input("Ingresa 1 números: "))

xxx = lambda a, b, c, : a * b + c
print(xxx(x,y,z))



# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as 
# an anonymous function inside another function.

# Say you have a function definition that takes one argument, 
# and that argument will be multiplied with an unknown number:

# Use that function definition to make a function that always 
# doubles the number you send in:

# Example
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(8)
print(mydoubler(int(input("Ingresa número: "))))

# Or, use the same function definition to make both functions, 
# in the same program:

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))