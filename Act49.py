#Write a program to check how the exceptions and finally statement works
try:
    Number1, Number2 = eval ( input ( " Enter 2 numbers separated by a comma : " ) )
    Result = Number1 / Number2
    print ( " Result is,", Result )
except ZeroDivisionError :
    print ( " ):!! DIVISION BY 0 IS ERROR !!:( " )
except SyntaxError :
    print ( " ! Comma is missing. Enter 2 numbers separated by a comma like this... (1, 2) ! " )
except :
    print ( " ! Wrong input ! " )
else :
    print ( " ! No exceptions ! " )
finally :
    print ( " !! This will execute no matter what !! " )