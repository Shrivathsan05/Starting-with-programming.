class IntegerToRomanNumeral() :
    def __init__(Self):
        pass
    def IntegerToRomanNumeral(Self, Number: int) -> str:
        RomanNumeralValues =[(4000000, 'I̅V̅'), (1000000, 'M̅'), (900000, 'C̅M̅'), (500000, 'D̅'), (400000, 'C̅D̅'), (100000, 'C̅'), (90000, 'X̅C̅'), (50000, 'L̅'), (40000, 'X̅L̅'), (10000, 'X̅'), (9000, 'I̅X̅'), (5000, 'V̅'), (4000, 'I̅V̅'), (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        TheRomanNumeral = ""
        for TheValue, TheSymbol in RomanNumeralValues:
            Counter, Number = divmod(Number, TheValue)
            TheRomanNumeral += TheSymbol * Counter
            if Number == 0:
                break      
        return TheRomanNumeral
TheIntegerShallBecomeARomanNumeral = IntegerToRomanNumeral()
TheIntegerWhichShallBecomeARomanNumeral = int(input(" Enter a number to be changed into a roman numeral! \n It must be less than or equal to 4,999,999! : "))
RomanNumeral = TheIntegerShallBecomeARomanNumeral.IntegerToRomanNumeral(TheIntegerWhichShallBecomeARomanNumeral)
print(f" The roman numeral for {TheIntegerWhichShallBecomeARomanNumeral} is: {RomanNumeral}")