#Write a program to perform the following operations: 1. Create a tuple with different datatypes 2. Create another tuple of integers 3. Create a new tuple by adding 9 to the previous tuple 4. Count the occurrences of an element in the tuple 5. Perform slicing on the tuple
TupleX = (" Tuple ", False, 3.2, 1)
print(TupleX)
TupleX = (4, 6, 2, 8, 3, 1)
print(TupleX)
TupleX = TupleX + (9,)
print(TupleX)
TupleX = (50, 10, 60, 70, 50)
print(TupleX.count(50))
TupleX = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
Slice = TupleX[3:5]
print(Slice)
Slice = TupleX[:6]
print(Slice)