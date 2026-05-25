#Create a tuple named weather with these elements - (1, 0, 0, 0, 1, 1, 0). If the element is 1 then the value of rainy increases by 1 otherwise the value of sunny increases by 1. On the basis of the value of rainy and sunny, predict the weather.
Weather = (1,0,0,0,1,1,0)
Sunny = 0
Rainy = 0
for s in range(0, 7):
    if (Weather[s]== 0):
        Rainy+=1
    else:
        Sunny+=1
if Sunny>Rainy:
    print(" Good Weather! ")
else:
    print(" Bad Weather! ")