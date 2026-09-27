while True:
    Infinity = 0
    print(" Hello! I am AI Bot, what is your name? ")
    UserName = input()
    print(f" Nice to meet you, {UserName}! ")
    print(f" What is your mood today, {UserName}? (Bad, Good, Neutral) ")
    Mood = input()
    if Mood == "Bad":
        print(" Do you want to end the chat? (Y/N) ")
        EndChat = input()
        if EndChat == "Y":
            while Infinity == 0:
                print(f" Have a good day, {UserName}! ")
                break
        if EndChat == "N":
            print(" Do you want to start over? (Y/N) ")
            StartOver = input()
            if StartOver == "N":
                while Infinity == 0:
                    print(f" Have a good day, {UserName}! ")
                    break
            if StartOver == "Y":
                continue            
    elif Mood == "Good":
        print(" Tell me some of your hobbies! ")
        Hobbies = input()
        if Hobbies != "":
            print(f" Thank you for telling me your hobbies! Farewell {UserName}! ")
        else:
            print(f" Farewell {UserName}! ")
    elif Mood == "Neutral":
        print(" Tell me some of your hobbies! ")
        Hobbies = input()
        if Hobbies != "":
            print(f" Thank you for telling me your hobbies! Farewell {UserName}! ")
        else:
            print(f" Farewell {UserName}! ")
    else:
        print(f" Farewell {UserName}! ")    
    break