import random
from colorama import init, Fore, Style
init(autoreset=True)
def DisplayBoard(Board):
    print()
    def ColorizeCell(Cell):
        if Cell == "X":
            return Fore.RED + Cell + Style.RESET_ALL
        elif Cell == "O":
            return Fore.BLUE + Cell + Style.RESET_ALL
        else:
            return Fore.YELLOW + Cell + Style.RESET_ALL
    print(" " + ColorizeCell(Board[0]) + " | " + ColorizeCell(Board[1]) + " | " + ColorizeCell(Board[2]))
    print(Fore.BLACK + "---+---+---")
    print(" " + ColorizeCell(Board[3]) + " | " + ColorizeCell(Board[4]) + " | " + ColorizeCell(Board[5]))
    print(Fore.BLACK + "---+---+---")
    print(" " + ColorizeCell(Board[6]) + " | " + ColorizeCell(Board[7]) + " | " + ColorizeCell(Board[8]))
    print()
def PlayerChoice():
    Symbol = ""
    while Symbol not in ["X", "O"]:
        Symbol = input(Fore.RED + "Player... Choose your symbol... X... or O... " + Style.RESET_ALL).upper()
    if Symbol == "X":
        return (" X ", " O ")
    else:
        return (" O ", " X ")
def PlayerMove(Board, Symbol):
    Move = -1
    while Move not in range(1, 10) or not Board[Move - 1].isdigit():
        try:
            Move = int(input(Fore.RED + " Player... Choose your move... 1... to 9... " + Style.RESET_ALL))
            if Move not in range(1, 10) or not Board[Move - 1].isdigit():
                print(Fore.RED + " Invalid move... Please... Try again... " + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + " Invalid input... Please... Enter a number... Between... 1... and... 9... " + Style.RESET_ALL)
    Board[Move - 1] = Symbol
def AIMove(Board, AISymbol, PlayerSymbol):
    for s in range(9):
        if Board[s].isdigit():
            BoardCopy = Board.copy()
            BoardCopy[s] = AISymbol
            if CheckWin(BoardCopy, AISymbol):
                Board[s] = AISymbol
                return
            Board[s] = str(s + 1)