#Write a program to calculate the sum of whole numbers.
Num = int(input("Enter the number whose sum you want to find : "))
Sum = 0
for Number in range (1, Num + 1):
    Sum = Sum + Number
    print ("\nSum =", Sum)

