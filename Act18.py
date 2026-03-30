#Write a program to show students' grades by entering five subject marks and calculating average marks and grades. For example, if the average is between 91 to 100, A2 is between 81 to 90, and so on, do it till grade E2?
print ("Enter marks obtained in 5 subjects: ")
Mark1 = int(input())
Mark2 = int(input())
Mark3 = int(input())
Mark4 = int(input())
Mark5 = int(input())
Total = Mark1+Mark2+Mark3+Mark4+Mark5
Average = Total/5
if Average >= 91 and Average <= 100:
    print ("Your grade is A1 !")
elif Average >= 81 and Average < 91:
    print ("Your grade is A2 !")
elif Average >= 71 and Average <81 :
    print ("Your grade is B1 !")
elif Average >= 61 and Average < 71 :
    print ("Your grade is B2 !")
elif Average >= 51 and Average < 61 :
    print ("Your grade is C1 !")
elif Average >= 41 and Average < 51 :
    print ("Your grade is C2 !")
elif Average >= 31 and Average < 41 :
    print ("Your grade is D1 !")
elif Average >= 21 and Average < 31 :
    print ("Your grade is D2 !")
elif Average >= 11 and Average < 21 :
    print ("Your grade is E1 !")
elif Average >= 1 and Average < 11 :
    print ("Your grade is E2 !")

