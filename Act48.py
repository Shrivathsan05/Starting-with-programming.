#Write a program to understand how the value error exception works?
try:
    Number = int ( input ( " Enter a number : " ) )
    print ( " The number entered is,", Number, "" )
except ValueError as Exception:
    print ( " Exception :", Exception )