#Write a program to demonstrate a Floyd triangle pattern?
Rows = int(input("Enter the total number of rows : "))
Number = 1
print ("Floyd's Triangle")
for NumberOfRows in range (1, Rows + 1) : 
    for NumberOfColumns in range (1, NumberOfRows + 1) : 
        print (Number, end = '  ')
        Number = Number + 1
    print ()

