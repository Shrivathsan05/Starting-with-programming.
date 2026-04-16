#Write a program to print all the prime numbers which come in the range entered by the user?
Lower = int(input("Enter a low range to start the list from : "))
Higher = int(input("Enter a high range to end the list with : "))
print ("Prime numbers from", Lower, "to", Higher, "are : ")
for Num in range (Lower, Higher +1) :
    if Num > 1 :
        for s in range (2,Num) :
            if ( Num % s ) == 0 :
                break
        else:
                print (Num)

