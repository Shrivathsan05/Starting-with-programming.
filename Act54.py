#Write a Python program to find the sum and average of the list. The average of the list is defined as the sum of the elements divided by the number of the elements. Also, find the largest and the smallest number in the list.
List = [4, 5, 1, 2, 9, 7, 10, 8]
print(" Original list :", List, "")
Count = 0
for s in List:
    Count += s
Average = Count/len(List)
print(" Sum =", Count, "")
print(" Average =", Average, "")
List.sort
print(" Smallest element is :", List[0])
print(" Largest element is :", List[-1])