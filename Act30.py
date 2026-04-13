#Write a program to check if the number entered by the user is an Armstrong number or not?
Num = int(input("Enter a number : "))
Sum = 0
Temp = Num
while Temp > 0 :
    Digit = Temp % 10
    Sum += Digit ** 3
    Temp //= 10
if Num == Sum :
    print(Num, "is an Armstrong number!:)(:")
else :
    print(Num, "is not an Armstrong number!:():")