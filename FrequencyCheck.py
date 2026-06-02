test_dict = {" Codingal " : 3, " is " : 2, " best " : 2, " for " : 2, " Coding " : 1}
print(" The original dictionary :", str(test_dict), "")
s = int(input(" Enter a number to check its occurences (3/2/1) : "))
res = 0
for key in test_dict:
    if test_dict[key] == s:
        res = res + 1
print(" Frequency of",  s,  "is : ", str(res), "")