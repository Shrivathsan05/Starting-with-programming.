def Cube (Number) :
    return Number * Number * Number
def By3 (Number) :
    if Number % 3 == 0 :
        return Cube (Number)
    else :
        return False
print (By3(9))
print (By3(4))

