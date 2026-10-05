import re, random
from colorama import Fore, init
init(autoreset=True)
print(Fore.GREEN + " I am Travel Bot! ")
Name = input(Fore.YELLOW + " What is your name? ")
Destinations = {" Beaches " : [" Maldives ", " Bora Bora ", " Santorini ", " Cayman Islands ", " Bali ", " Hawaii ", " Phuket "], " Mountains " : [" Swiss Alps ", " Rocky Mountains ", " Himalayas "], " Cities " : [" Paris ", " New York ", " Tokyo "]}
Jokes = [" Why don't programmers like nature? It has too many bugs! ", " Why do programmers prefer dark mode? Because light attracts bugs! ", " What is a programmer's favorite snack? Microchips! ", " Why do programmers always mix up Halloween and Christmas? Because Oct 31 == Dec 25! ", " Why did the computer go to the doctor? Because it had a virus! ", " Why do travellers always feel warm? Because they carry their own sunshine, and because of all of their hot spots! "]
def NormalizeInput(Text):
    return re.sub(r"\s+", " ", Text.strip().lower())
def RecommendDestination():
    print(Fore.YELLOW + " Trav : Beaches, Mountains, Or Cities? ")
    Preference = Name + input(Fore.RED + " Your choice: ")
    Preference = NormalizeInput(Preference)
    if Preference in Destinations:
        Suggestion = random.choice(Destinations[Preference])
        print(Fore.GREEN + f" Trav : I suggest you visit {Suggestion}!")
def TellJoke():
    return random.choice(Jokes)