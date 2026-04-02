#Write to check a number is divisible by another number.
print("Enter a number (Numerator): ")
NumberNumerator = int(input())
print("Enter a number (Denominator): ")
NumberDenominator = int(input())
if NumberNumerator%NumberDenominator == 0:
    print("\n" +str(NumberNumerator)+ " is divisible by " +str(NumberDenominator))
else:
    print("\n" +str(NumberNumerator)+ " is not divisible by " +str(NumberDenominator))