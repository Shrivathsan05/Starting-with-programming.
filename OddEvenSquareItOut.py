StartNumber = int(input("Enter the number whose power you start with : "))
EndNumber = int(input("Enter the number whose power you end with : "))
Output = 1
Evelist = "List of Even Squares: "
Oddlist = "List of Odd Squares: "
for Num in range(StartNumber, EndNumber + 1):
    Output = Num * Num
    if Output % 2 == 0:
        Evelist = Evelist + str(Output) + " "
    else:
        Oddlist = Oddlist + str(Output) + " "  
    print("\nOutput =", Output)
print("\n" + Evelist)
print(Oddlist)


