Num = int(input("Enter a decimal integer that you want to convert to Binary : "))
Quotient, Remainder = divmod(Num, 2)
Binary = str(Remainder)
while Quotient != 0 :
    Quotient, Remainder = divmod(Quotient, 2)
    Binary = str(Remainder) + Binary   
print (Binary) 

