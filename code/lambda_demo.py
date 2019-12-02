#A lambda function is a small anonymous function.

#A lambda function can take any number of arguments, but can only have one expression.

# write a code that adds 10 to a number

def add10(a_number):
	return a_number + 10

print(add10(30))

x = lambda a : a + 10
print(x(30))

# write a lambda function to returns square,factorial

square = lambda a : a*a
print(square(4))


fact = lambda x: 1 if x == 0 else x * fact(x-1)
print(fact(4))



# task for you
# write a calculator with lambda functions for calculator operators
# implement addition, substraction, division, multiplication

