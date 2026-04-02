d = int(input("Enter 1st value."))
c = int(input("Enter 2nd value."))
b = int(input("Enter 3rd value."))
print("(",d, " + ", c,") / ", b, " = ", (d+c)/b)
a = str(input("Is this the anwser you were expecting?(Yes or No)"))
if a == "Yes":
    print("Thank you! Danke!")
else:
    e = str(input("What is wrong?Do you want to swap the numbers?(Yes or No)"))
    if e == "Yes":
        print("(",b, " + ", d,") / ", c, " = ", (b+d)/c)
        f = str(input("Is this the anwser you were expecting?(Yes or No)"))
        if f == "Yes":
            print("Thank you! Danke!")
        else:
            g = str(input("What is wrong?Do you want to swap the numbers?(Yes or No)"))
            if g == "Yes":
                print("(",c, " + ", b,") / ", d, " = ", (c+b)/d)
            else:
                print("Thank you! Danke!")