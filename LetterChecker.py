import string

UserLetter = str(input("Enter a character!"))

if UserLetter in string.ascii_letters :
    print (UserLetter, "is an alphabet!")
else:
    print (UserLetter, "is not an alphabet!")