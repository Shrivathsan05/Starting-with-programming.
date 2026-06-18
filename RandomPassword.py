import random
Numbers = "0123456789"
Letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
AllSymbols = "~!@#$%^&*()_+-={}[]|/:;>.<,"
RandomNumber1 = random.randint(1, 20)
RandomNumber2 = random.randint(1, 3)
Int = random.randint(0, 9)
Str = ''.join(random.choices(Letters, k=6))
Symbols = ''.join(random.choices(AllSymbols, k=4))
Joined1st = str(Int) + Str + Symbols
MinimumLength = 8
while True:
    FirstPassword = "".join(random.choices(Joined1st, k= RandomNumber1))
    Joined2nd = str(Int) + Str + Symbols
    SecondPassword = "".join(random.choices(Joined2nd, k= RandomNumber2))
    if len(FirstPassword) >= MinimumLength:
        break
print(" This is the first password (min length of 8):", FirstPassword)
print(" This is the second password (no min length):", SecondPassword)

