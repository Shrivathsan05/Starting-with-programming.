import time, panadas as pd
from textblob import TextBlob
from colorama import init, Fore
init(autoreset=True)
try : Movies = pd.read_csv("imdb_top_1000.csv")
except FileNotFoundError:
    print(Fore.RED + " Error : File not found. 'imdb_top_1000.csv' was not found. ") ; raise SystemExit
Genres = sorted({s.strip() for sublist in Movies[" Genre "].dropna().str.split(" , ") for s in sublist})
def Dots():
    for k in range(3) : print(Fore.YELLOW + " . ", end="", flush=True) ;
time.sleep(0.5)
def Sentiment(Feeling): return " Positive! ☺︎😁☺︎ " if Feeling > 0 else " Negative!  ☹😭☹ " if Feeling < 0 else " Neutral -_-😐-_- "
def Reccommendation(Genre, Feeling):
    if Feeling > 0 : return Movies[Movies[" Genre "].str.contains(Genre)].sort_values(" IMDB Rating ", ascending=False).head(5)[[" Series_Title ", " IMDB Rating "]]
    elif Feeling < 0 : return Movies[Movies[" Genre "].str.contains(Genre)].sort_values(" IMDB Rating ", ascending=True).head(5)[[" Series_Title ", " IMDB Rating "]]
    else : return Movies[Movies[" Genre "].str.contains(Genre)].sample(5)[[" Series_Title ", " IMDB Rating "]]