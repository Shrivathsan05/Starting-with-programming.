import colorama
from colorama import Fore, Style
from textblob import TextBlob
colorama.init()
print(f"{Fore.GREEN} 🕵🏻 Welcome To Sentiment Spy! 🕵🏻 {Style.RESET_ALL}")
UserName = input(f"{Fore.LIGHTRED_EX} Pls Enter Your Name : {Style.RESET_ALL}").strip()
if not UserName :
    UserName = " ???? Mystery Agent ???? "
ConversationHistory = []
print(f"\n{Fore.RED} Hello Agent {UserName}! ")
print(f"{Fore.BLUE} Type A Sentence & I Will Analyze Your Sentences With TextBlob & Show You The Sentiment! ")
print(f" Type {Fore.LIGHTRED_EX} Reset {Fore.RED}, {Fore.LIGHTRED_EX} History {Fore.RED}, "f" Or {Fore.LIGHTRED_EX} Exit {Fore.RED} To Quit! {Style.RESET_ALL}\n")
while True :
    UserInput = input(f" {Fore.RED}>>> {Style.RESET_ALL}").strip()
    if not UserInput:
        print(f"{Fore.RED} Please Enter Some Text Or A Valid Command! {Style.RESET_ALL}")
        continue
    if UserInput.lower() == "exit":
        print(f"\n{Fore.YELLOW} Exiting Sentiment Spy Farewell, Agent {UserName}! {Style.RESET_ALL}")
        break
    elif UserInput.lower() == "reset":
        ConversationHistory.clear()
        print(f"{Fore.GREEN} Conversation history has been reset! {Style.RESET_ALL}")
    elif UserInput.lower() == "history":
        if not ConversationHistory:
            print(f"{Fore.RED} No conversation history available. {Style.RESET_ALL}")
        else:
            print(f"{Fore.BLUE} Conversation History: {Style.RESET_ALL}")
            for idx, (text, polarity, sentiment_type) in enumerate(ConversationHistory, start=1):
                if sentiment_type == "Positive":
                    color = Fore.GREEN
                    emoji = "😊"
                elif sentiment_type == "Negative":
                    color = Fore.RED
                    emoji = "😢"
                else:
                    color = Fore.YELLOW
                    emoji = "😐"
                print(f"{idx}. {color}{emoji} {text} "f"(Polarity: {polarity:.2f}, {sentiment_type}){Style.RESET_ALL}")
            continue
    polarity = TextBlob(UserInput).sentiment.polarity
    if polarity > 0.25:
        sentiment_type = "Positive"
        color = Fore.GREEN
        emoji = "😊"
    elif polarity < -0.25:
        sentiment_type = "Negative"
        color = Fore.RED
        emoji = "😢"
    else:
        sentiment_type = "Neutral"
        color = Fore.YELLOW
        emoji = "😐"

    ConversationHistory.append((UserInput, polarity, sentiment_type))
    print(f"{color}{emoji} {sentiment_type} sentiment detected! "f"(Polarity: {polarity:.2f}){Style.RESET_ALL}")