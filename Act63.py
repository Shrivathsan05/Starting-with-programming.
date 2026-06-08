#Write a program to return the addition of numbers of two different lists. Then, display a list that is square of numbers of another list. Use the map() function here to get the desired result.
Numbers1 = [1, 2, 3]
Numbers2 = [4, 5, 6]
Result = map(lambda X, Y : X + Y, Numbers1, Numbers2)
print(" Addition of 2 lists! ")
print(list(Result))
Numbers = [1, 2, 3, 4, 5]
def sq(S) :
    return S * S
Square = list(map(sq, Numbers))
print(" Square of numbers in list! ")
print(Square)