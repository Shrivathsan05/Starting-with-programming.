Tuple = input(" Give me a tuple of numbers to multiply with commas in between each number! ")
Tuple = tuple(int(Number.strip()) for Number in Tuple.split(","))
TupleProduct = 1
for Value in Tuple:
    TupleProduct = TupleProduct*Value
TupleLength = len((Tuple))
print(" There are", TupleLength, "value(s) in the tuple you inputted! ")
print(" Here is the product of all the values in your tuple multiplied :",int(TupleProduct))