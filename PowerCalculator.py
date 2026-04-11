Number = int(input("Enter the number whose power you want to find : "))
Power = int(input("Enter the power you want to get to : "))
Output = 1
for Num in range (1, Power + 1):
    Output = Output * Number
print ("\nOutput =", Output)
