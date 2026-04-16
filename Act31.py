#Write a program to check how many times a character is repeated in a word?
String = input("Enter your own word : ")
Character = input("Enter your own character (letter) : ")
s = 0
Count = 0
while (s < len(String)) :
    if (String[s] == Character) :
        Count = Count + 1
    s = s + 1
print ("The total number of times", Character, "has occured in", String, "is,", Count)

