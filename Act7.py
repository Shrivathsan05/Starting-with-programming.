

#Write a program to calculate the number of notes in the given amount?
#Taking total amount as input from user
Amount = int(input("Please enter amount for withdraw : "))

#Calculating the number of notes of different denominations
Note1 = Amount//100
Note2 = (Amount%100)//50
Note3 = ((Amount%100)//50)//10

print  ("Notes of 100 Rupee", Note1)
print  ("Notes of 50 Rupee", Note2)
print  ("Notes of 10 Rupee", Note3)

