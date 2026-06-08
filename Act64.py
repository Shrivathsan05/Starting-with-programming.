#Write a program to return - 1. zipped list from two lists 2. elements of two lists zipped together, but 2nd list in reverse order 3. elements of two lists zipped into a dictionary
SsZz1 = {2 , 3 , 1}
SsZz2 = {" B " , " A " , " C "}
SsZz3 = list(zip(SsZz1 , SsZz2))
print(SsZz3 , " \n ")
List1 = [10 , 20 , 30 , 40]
List2 = [100 , 200 , 300 , 400]
for xS , yS in zip(List1 , List2[::-1]) :
    print(xS , yS)
Stocks = [" Reliance " , " InfoSys " , " TCS "]
Prices = [2175 , 1127 , 2750]
NewDictionary = {Stocks : Prices for Stocks , Prices in zip(Stocks , Prices)}
print("\n{}".format(NewDictionary))