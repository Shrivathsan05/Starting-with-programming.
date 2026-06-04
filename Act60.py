#Write a program to create a set and perform the following operations on that set- 1. Create a set with integer elements 2. Create a set with mixed data type elements 3. Create another set with elements - 1, 2, 3, 4, 3, 2 4. Create a set from a list with elements - [1, 2, 3, 2] 5. Print the set after removing the first element from this set - [0, 1, 3, 4, 5]
MySet = {1, 2, 3}
print(MySet)

MySet = {1.0, " Hello ", (1, 2, 3)}
print(MySet)

MySet = {1, 2, 3, 4, 3, 2}
print(MySet)

MySet = set([1, 2, 3, 2])
print(MySet, " \n ")

NumberSet = set([0, 1, 3, 4, 5])
print(" Original set : ")

print(NumberSet)
NumberSet.pop()
print(" After removing the 1st element from the said set : ")
print(NumberSet, " \n ")