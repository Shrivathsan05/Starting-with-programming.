print(" Lets play Rock Paper Scissors! ")
def PlayerChoice():
    choice = input("Choose Rock, Paper, or Scissors: ").capitalize()
    while choice not in ["Rock", "Paper", "Scissors"]:
        choice = input("Invalid choice. Please choose Rock, Paper, or Scissors: ").capitalize()
    return choice
def ComputerChoice():
    import random
    return random.choice(["Rock", "Paper", "Scissors"])
def DetermineWinner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "Rock" and computer == "Scissors") or (player == "Paper" and computer == "Rock") or (player == "Scissors" and computer == "Paper"):
        return "You win!"
    else:
        return "Computer wins!"
def start_rps_game():
    player_choice = PlayerChoice()
    computer_choice = ComputerChoice()
    print(f"You chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")
    result = DetermineWinner(player_choice, computer_choice)
    print(result)
def InfinetlyPlay():
    while True:
        start_rps_game()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break
        if play_again == "yes":
            start_rps_game()
InfinetlyPlay()