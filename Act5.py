#Write a program to print the “CODINGAL” word in a reverse direction.
#input a word
Text = str(input("Enter a String: "))

#Reverse String
#using step value as -1 to iterate in reverse
RevText=Text[::-1]
Text=RevText

print("Reverse of given string is:")
print(Text)

