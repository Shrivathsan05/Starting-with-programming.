import time, pandas as pd
from textblob import TextBlob
from colorama import init, Fore
init(autoreset=True)
try : Movies = pd.read_csv("imdb_top_1000.csv")
except FileNotFoundError:
    print(Fore.RED + " Error : File not found. 'imdb_top_1000.csv' was not found. ") ; raise SystemExit
Genres = sorted({s.strip() for sublist in Movies["Genre"].dropna().str.split(", ") for s in sublist})
def Dots():
    for k in range(3) : print(Fore.YELLOW + " . ", end="", flush=True) ;
time.sleep(0.5)
def Sentiment(Feeling): return " Positive! ☺︎😁☺︎ " if Feeling > 0 else " Negative!  ☹😭☹ " if Feeling < 0 else " Neutral -_-😐-_- "
def recommend(Genre=None, Mood=None, Rating=None, s=5):
    MoviesCopy = Movies
    if Genre: MoviesCopy = MoviesCopy[MoviesCopy["Genre"].str.contains(Genre, case=False, na=False)]
    if Rating is not None: MoviesCopy = MoviesCopy[MoviesCopy["IMDB_Rating"] >= Rating]
    if MoviesCopy.empty: return "No suitable movie recommendations found."
    MoviesCopy, need_nonneg, out = MoviesCopy.sample(frac=1).reset_index(drop=True), bool(Mood), []
    for _, r in MoviesCopy.iterrows():
        ov = r.get("Overview")
        if pd.isna(ov): continue
        pol = TextBlob(ov).sentiment.polarity
        if (not need_nonneg) or pol >= 0:
            out.append((r["Series_Title"], pol))
            if len(out) == s: break
    return out if out else "No suitable movie recommendations found."
def show(recs, name):
    print(Fore.YELLOW + f"\n🍿 AI-Analyzed Movie Recommendations for {name}:")
    for i, (t, p) in enumerate(recs, 1):
        print(f"{Fore.CYAN}{i}. 🎥 {t} (Polarity: {p:.2f}, {Sentiment(p)})")
def get_genre():
    print(Fore.GREEN + "Available Genres: ", end="")
    for i, g in enumerate(Genres, 1): print(f"{Fore.CYAN}{i}. {g}")
    print()
    while True:
        x = input(Fore.YELLOW + "Enter genre number or name: ").strip()
        if x.isdigit() and 1 <= int(x) <= len(Genres): return Genres[int(x) - 1]
        x = x.title()
        if x in Genres: return x
        print(Fore.RED + "Invalid input. Try again.\n")
def get_rating():
    while True:
        x = input(Fore.YELLOW + "Enter minimum IMDB rating (7.6-9.3) or 'skip': ").strip()
        if x.lower() == "skip": return None
        try:
            r = float(x)
            if 7.6 <= r <= 9.3: return r
            print(Fore.RED + "Rating out of range. Try again.\n")
        except ValueError:
            print(Fore.RED + "Invalid input. Try again.\n")
print(Fore.BLUE + "🎥 Welcome to your Personal Movie Recommendation Assistant! 🎥\n")
name = input(Fore.YELLOW + "What's your name? ").strip()
print(f"\n{Fore.GREEN}Great to meet you, {name}!\n")
print(Fore.BLUE + "\n🔍 Let's find the perfect movie for you!\n")
genre = get_genre()
mood = input(Fore.YELLOW + "How do you feel today? (Describe your mood): ").strip()
print(Fore.BLUE + "\nAnalyzing mood", end="", flush=True); Dots()
mp = TextBlob(mood).sentiment.polarity
md = "positive 😊" if mp > 0 else "negative 😞" if mp < 0 else "neutral 😐"
print(f"\n{Fore.GREEN}Your mood is {md} (Polarity: {mp:.2f}).\n")
rating = get_rating()
print(f"{Fore.BLUE}\nFinding movies for {name}", end="", flush=True); Dots()
recs = recommend(Genre=genre, Mood=mood, Rating=rating, s=5)
print(Fore.RED + recs + "\n") if isinstance(recs, str) else show(recs, name)
while True:
    a = input(Fore.YELLOW + "\nWould you like more recommendations? (yes/no): ").strip().lower()
    if a == "no":
        print(Fore.GREEN + f"\nEnjoy your movie picks, {name}! 🎬🍿\n"); break
    if a == "yes":
        recs = recommend(Genre=genre, Mood=mood, Rating=rating, s=5)
        print(Fore.RED + recs + "\n") if isinstance(recs, str) else show(recs, name)
    else:
        print(Fore.RED + "Invalid choice. Try again.\n")