#Raj scored 40, 70, 50 and 60 out of 100 in maths, science, Hindi and English. Find the percentage he got?
# Take marks as input from the user
print ("Enter marks obtained in 4 subjects!")
Math = int(input("Math Score Percent: "))
English = int(input("English Score Percent: "))
Science = int(input("Science Score Percent: "))
Hindi = int(input("Hindi Score Percent: "))

#Lets calculate the percentage of the marks
Sum = Math+English+Hindi+Science
print ("The sum of your Math, English, Science,& Hindi test scores is ", Sum)

Percent = (Sum/400)*100

print (end="Mark Percentage = ")
print (Percent)

