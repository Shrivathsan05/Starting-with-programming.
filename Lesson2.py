import colorama
from colorama import Fore, Style
from textblob import Textblob
colorama.init()
print(f"{Fore.RED} 🕵🏻 Welcome To Sentiment Spy! 🕵🏻 {Style.RESET_ALL}")
UserName = input(f"{Fore.LIGHTRED_EX} Pls Enter Your Name : ___________ {Style.RESET_ALL}").strip()
if not UserName :
    UserName = " ???? Mystery Agent ???? "
ConversationHistory = []
print(f"\n{Fore.RED} Hello Agent {UserName}! ")
print(f" Type A Sentence & I Will Analyze Your Sentences With TextBlob & Show You The Sentiment! ")
print(f" Type {Fore.LIGHTRED_EX} Reset {Fore.RED}, {Fore.LIGHTRED_EX} History {Fore.RED}, "f" Or {Fore.LIGHTRED_EX} Exit {Fore.RED} To Quit! {Style.RESET_ALL}\n")
while True :
    UserInput = input(f" {Fore.RED}>>> ")