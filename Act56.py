#Write a program to check whether the given tuple - (1,2,3,3,2,1) is a palindrome or not. If it's a palindrome, then it is the same after being reversed.
def Palindrome(S):
    k = len(S) -1
    g = 0
    while g<k:
        if(S[k]!=S[g]):
            return False
        g+=1
        k-=1
    return True
s = (1,2,3,3,2,1)
if Palindrome(s):
    print(" The Tuple Is Flip-Flopped! ")
else:
    print(" The Tuple Is Not Flip-Flopped! ")