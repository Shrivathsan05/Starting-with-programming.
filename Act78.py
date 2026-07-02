#Write a program to create two classes for two different countries that consist of three methods to display the following information of respective country - capital, language and type of country. Then, use Polymorphism to create a common interface for both classes.
class INDIA() :
    def Capital(Self) :
        print(" New Delhi is the capital of India! ")
    def Language(Self) :
        print(" Hindi is the most widely spoken language of India! ")
    def DevelopType(Self) :
        print(" India is a developing country! ")
class USA() :
    def Capital(Self) :
        print(" Washington D.C. is the capital of the USA! ")
    def Language(Self) :
        print(" English is the primary language of the USA! ")
    def DevelopType(Self) :
        print(" USA is a developed country! ")
INDIAObjOfIndia = INDIA()
USAObjOfTheUSA = USA()
for Country in (INDIAObjOfIndia, USAObjOfTheUSA) :
    Country.Capital()
    Country.Language()
    Country.DevelopType()