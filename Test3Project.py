import random
GradeBook = {" Raj " : 92, " Sai " : 99, " Shri " : 100, " Shilaja " : 54, " Shreya " : 49}
ClassAverage = " The class average :", GradeBook[" Raj "] * GradeBook[" Sai " ] * GradeBook[" Shilaja "] * GradeBook[" Shreya "] * GradeBook[" Shri "] / 5
TopScorer = " The top scorer, Shri! Points :", GradeBook[" Shri "]
BottomScorer = " The bottom scorer, Shreya! Points :", GradeBook[" Shreya "]
print(GradeBook, ClassAverage, TopScorer, BottomScorer)