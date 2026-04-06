print ("Are you here to enroll? (Y/N) : ") 
EnrollYesOrNO = str(input()).strip().upper()
if EnrollYesOrNO == "Y":
    Name = input("What is your full name?")
    Age10 = str(input("Are you over 10? (Y/N) : "))
    if Age10 == "Y":
        Age20 = str(input("Great! Are you under 20? (Y/N) : "))
        if Age20 == "Y":
            print ("Great! Then you can enroll!")
            Age = int(input("What is your age?"))
            if 20 >= Age >= 10 :
                print ("Thank you for enrolling! Our database has now stored that the age of",Name,"is",Age,"!" )
            else:
                print ("Oh. Sorry, but you can't enroll. Bye bye then!")
        else:
            print ("Oh. Sorry, but you can't enroll. Bye bye then!")
    else:
        print ("Oh. Sorry, but you can't enroll. Bye bye then!")
else:
    print ("Bye bye then!")