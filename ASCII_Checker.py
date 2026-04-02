Letter = input("Enter a single character: ")
if type(Letter) is str and len(Letter) == 1:
    print("Valid input!")
    ASCII = ord(Letter)
    print(f"Character: {Letter}")
    print(f"ASCII Value: {ASCII}")
    if ASCII >= 65 and ASCII <= 90:
        print("Type: Uppercase Letter")
    elif ASCII >= 97 and ASCII <= 122:
        print("Type: Lowercase Letter")
    elif ASCII >= 48 and ASCII <= 57:
        print("Type: Digit")
    elif ASCII == 32:
        print("Type: Space")
    else:
        print("Type: Special Character")

else:
    print("Please enter exactly 1 character!")

