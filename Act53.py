#Write a Python program to count the number of strings where the string length is two or more, and the first and last characters are the same from a given list of strings.
def MatchWords(Words):
    Counter = 0
    List = []
    for Word in Words:
        if len(Word) > 1 and Word[0] == Word[-1]:
            Counter += 1
            List.append(Word)
    print(" List of words with first and last character same\n", List, "")
    return Counter
Count = MatchWords([" ABC ", " CFC ", " XYZ ", " ABA ", " 1221 "])
print(" Number of words having first and last character same :", Count)