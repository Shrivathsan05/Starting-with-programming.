import re, random
from colorama import Fore, init
init(autoreset=True)
print(Fore.GREEN + " Travel Bot : I am Travel Bot! You can call me Travax0t! ")
Name = input(Fore.LIGHTYELLOW_EX + " Travax0t : What is your name? (Just your name) \n")
print(Fore.GREEN + f" Travax0t : Nice to meet you, {Name}! ")
Destinations = {"beaches" : [" Maldives ", " Bora Bora ", " Santorini ", " Cayman Islands ", " Bali ", " Hawaii ", " Phuket "], "mountains" : [" The Swiss Alps ", " The Rocky Mountains ", " The Himalayas "], "cities" : [" Paris ", " New York ", " Tokyo "]}
Jokes = [" Why don't programmers like nature? It has too many bugs! ", " Why do programmers prefer dark mode? Because light attracts bugs! ", " What is a programmer's favorite snack? Microchips! ", " Why do programmers always mix up Halloween and Christmas? Because Oct 31 == Dec 25! ", " Why did the computer go to the doctor? Because it had a virus! ", " Why do travellers always feel warm? Because they carry their own sunshine, and because of all of their hot spots! "]
def NormalizeInput(Text):
    return re.sub(r"\s+", " ", Text.strip().lower())
def RecommendDestination():
    print(Fore.LIGHTYELLOW_EX + " Travax0t : Do you want to visit Beaches, Mountains, Or Cities? ")
    Preference = input(Fore.RED + " " + Name + " : ")
    Preference = NormalizeInput(Preference)
    print (Fore.GREEN + f" Travax0t : You chose {Preference}. Let me find a destination for you! ")
    if Preference in Destinations:
        Suggestion = random.choice(Destinations[Preference])
        print(Fore.GREEN + f" Travax0t : I suggest you visit {Suggestion}!")
        print(Fore.LIGHTYELLOW_EX + " Travax0t : Do you like this suggestion? (Y/N) ")
        Answer = input(Fore.RED + " " + Name + " : ").capitalize()
        if Answer == "Y":
            print(Fore.GREEN + " Travax0t : Great! I hope you have a wonderful trip! Enjoy your travels to " + Suggestion + "! ")
        elif Answer == "N":
            print(Fore.YELLOW + " Travax0t : No worries! Let's try again. ")
            RecommendDestination()
        else:
            print(Fore.YELLOW + " Travax0t : I didn't understand that. Let's try again. ")
            RecommendDestination()
    else:
        print(Fore.YELLOW + " Travax0t : I don't have a destination like that. Let's try again. ")
        RecommendDestination()
def PackingTips():
    print(Fore.GREEN + " Travax0t : Here are some packing tips for your trip: ")
    print(Fore.GREEN + " 1. Make a packing list to ensure you don't forget anything. ")
    print(Fore.GREEN + " 2. Pack versatile clothing that can be mixed and matched. ")
    print(Fore.GREEN + " 3. Roll your clothes to save space and reduce wrinkles. ")
    print(Fore.GREEN + " 4. Don't forget essential items like chargers, toiletries, and medications. ")
    print(Fore.GREEN + " 5. Check the weather forecast for your destination and pack accordingly. ")    
def TellJoke():
    print(Fore.GREEN + " Travax0t : Here's a joke for you : " + random.choice(Jokes))
def ShowHelp():
    print(Fore.GREEN + " Travax0t : Here are some things you can ask me to do: ")
    print(Fore.GREEN + " 1. Type ' Recommendation ' - I can suggest a travel destination based on your preferences. ")
    print(Fore.GREEN + " 2. Type ' Packing  ' - I can provide you with useful packing tips for your trip. ")
    print(Fore.GREEN + " 3. Type ' Joke ' - I can tell you a joke to lighten the mood. ")
    print(Fore.GREEN + " 4. Type ' Help ' - I can show you this help message again if you need it. ")
    print(Fore.GREEN + " 5. Type ' Exit ' - I can end our conversation if you want to stop talking. ")
def Chat():
    ShowHelp()
    while True:
        UserInput = input(Fore.RED + " " + Name + " : ")
        UserInput = NormalizeInput(UserInput)
        if UserInput == "recommendation" or UserInput == " recommendation ":
            RecommendDestination()
        elif UserInput == "packing" or UserInput == " packing ":
            PackingTips()
        elif UserInput == "joke" or UserInput == " joke ":
            TellJoke()
        elif UserInput == "help" or UserInput == " help ":
            ShowHelp()
        elif UserInput == "exit" or UserInput == " exit ":
            print(Fore.GREEN + f" Travax0t : Goodbye, {Name}! Safe travels! ")
            break
        else:
            print(Fore.YELLOW + " Travax0t : I'm sorry, I didn't understand that. Please try again or type 'Help' for options. ")
if __name__ == "__main__":
    Chat()