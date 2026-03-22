import math
Number = int(input("What is the number you are trying to find the Sq root of?"))
FloatVsInt = str(input("Do you want Integer or Floating value as your answer?"))
if FloatVsInt == "Integer":
    SqRoot = math.isqrt(Number)
    print(f"The Sq root of {Number} is {SqRoot}")
else:
    SqRoot1 = math.sqrt(Number)
    print(f"The Sq root of {Number} is {SqRoot1}")

