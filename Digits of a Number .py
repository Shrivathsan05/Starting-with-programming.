Number = int(input("Enter a number : "))
Digits = 0
while Number > 0 :
    Digits = Digits + 1
    Number, Remainder = divmod(Number, 10)
print ("Your number has",Digits, "digits!")