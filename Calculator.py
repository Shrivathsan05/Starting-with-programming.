def Addition(S, A):
    return(S + A)
def Subtraction(S, A):
    return(S - A)
def Multiplication(S, A):
    return(S * A)
def Division(S, A):
    return(S / A)
OpType = input(" Is your operation float(F) or integer(I)? (F/I) ")
SiType = input(" Addition(A), Subtraction(S), Multiplication(M), or Division(D)? (A/S/M/D) ")
if OpType == "I":
    First = int(input(" Enter your first number : "))
    Second = int(input(" Enter your second number : "))
    if SiType == "A":
        Result = Addition(First, Second)
    elif SiType == "S":
        Result = Subtraction(First, Second)
    elif SiType == "M":
        Result = Multiplication(First, Second)
    elif SiType == "D":
        Result = Division(First, Second)
    else:
        print(" Unknown ")
if OpType == "F":
    First = float(input(" Enter your first number : "))
    Second = float(input(" Enter your second number : "))
    if SiType == "A":
        Result = Addition(First, Second)
    elif SiType == "S":
        Result = Subtraction(First, Second)
    elif SiType == "M":
        Result = Multiplication(First, Second)
    elif SiType == "D":
        Result = Division(First, Second)
    else:
        print(" Unknown ")
print(Result)