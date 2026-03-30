#Write a program to illustrate the use of 'is' identity operator
#Python program to illustrate use
# of 'is' identity operator

X = 5
if (type (X) is int):
    print ("True")
else:
    print("False!")
X = 5.5
if (type (X) is not float):
    print ("True")
else:
    print("False!")
X = 20
Y = 20
if (X is Y):
    print("X & Y have the same identity!")
X = 30
if (X is not Y):
    print("X & Y have different identities!")

