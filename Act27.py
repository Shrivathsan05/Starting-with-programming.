#Write a program to print the numbers in reverse order beginning from the number entered by the user.
Number = int(input("Enter the value of the number : "))
print ("Numbers from {0} to {1} are : ".format(Number,1))
for i in range (Number,0,-1):
    print (i)

