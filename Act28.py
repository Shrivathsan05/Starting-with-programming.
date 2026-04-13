#Write a program to find the sum of natural numbers.
Num = int(input("Enter the number of terms : "))
Sum = 0
Number = 1
while Number <= Num :
    Sum = Sum + Number
    Number = Number + 1
print("\nSum =", Sum)

