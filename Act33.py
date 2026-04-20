#Write a program to demonstrate a right angle triangle pattern?
print ("Half Pyramid Pattern of Stars (*) : ")
NumberOfRows = int(input("Enter the Number of Rows : "))
for NumberOfColumns in range (NumberOfRows) : 
    for Result in range (NumberOfColumns + 1) : 
        print ("* ", end="")
    print ()

