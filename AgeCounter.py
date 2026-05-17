Age = input(" Enter a number : ")
if Age.isdigit():
    Age = int(Age)
    if Age % 2 == 0 :
        print("", Age, "is not an odd number, it is an even number! ")
    else :
        print("", Age, "is not an even number, it is an odd number! ")
else:
    print("", Age, "is not even a number! ")
