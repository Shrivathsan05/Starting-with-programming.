#The mean of 40 numbers is 38. Later on, I detected that I misread the number 56 as 36. Find the correct mean of given numbers.
Mean = 38
WrongNumber = 36
CorrectNumber = 56
TotalNumber = 40
#Sum of 40 numbers
Sum = Mean*TotalNumber
print("The sum of 40 number : ",Sum)
#Correct sum of these numbers
Number = Sum-((WrongNumber)-(CorrectNumber))
print("Sum-((WrongNumber)-(CorrectNumber)) : ",Number)
#The correct mean
TheTrueCorrectMean = Number/TotalNumber
print(TheTrueCorrectMean)