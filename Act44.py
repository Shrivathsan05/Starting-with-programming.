#Write a program to find the factorial using recursive function
def Factorial (X) :
    """ This is a recursive function to find the factorial of an integer """
    if X == 0 or X == 1 :
        return 1
    else :
        return X * Factorial (X - 1)
print (Factorial.__doc__)
print (" The Factorial of 0 :", Factorial(0))
print (" The Factorial of 1 :", Factorial(1))
print (" The Factorial of 2 :", Factorial(2))
print (" The Factorial of 5 :", Factorial(5))
print (" The Factorial of 10 :", Factorial(10))

