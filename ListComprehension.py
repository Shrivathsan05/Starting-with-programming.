Integer = int(input(" Enter a number : "))
AllNumbersBelowInteger = range(Integer)
Int = 0
AllOddNumbersBelowInteger = ""
for Int in range(Integer) :
    if Int % 2 != 0:
        if AllOddNumbersBelowInteger == "":
            AllOddNumbersBelowInteger = str(Int)
        else:
            AllOddNumbersBelowInteger = str(AllOddNumbersBelowInteger) + ", " + str(Int)
    Int = Int + 1
print(AllOddNumbersBelowInteger)

FruitsLowercaseLetters = [" 🍊 citrus : " , " grapefruit " , " lemon " , " lime " , " mandarin " , " orange " , " tangerine " , " 🍓 berries : " , " blackberry " , " blueberry " , " cranberry " , " grape " , " raspberry " , " strawberry " , " 🍎 pomes (core/seed) : " , " apple " , " pear " , " quince " , " 🍑 stone fruits (drupes) " , " apricot " , " cherry " , " nectarine " , " peach " , " plum " , " 🍈 Melons : " , " cantaloupe " , " honeydew " , " watermelon " , " 🥭 tropical & exotic " , " banana " , " dragon fruit " , " kiwi " , " mango " , " papaya " , " pineapple " , " pomegranate "]
print(" Lowercase :", FruitsLowercaseLetters, "")
FruitsUppercaseLetters = [Fruit.title() for Fruit in FruitsLowercaseLetters]
print("\n\n Uppercase :", FruitsUppercaseLetters, "")