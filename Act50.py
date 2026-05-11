#Write a program using nested while loop. If the value is divided by two, then it will run an infinite loop of the bye.
Valid = False
while not Valid :
    try :
        Number = int ( input ( " Enter a number : " ) )
        while Number%2==0 :
            print ( " ! BYE ! " )
        Valid = True
    except ValueError :
        print ( " ! Invalid ! " )