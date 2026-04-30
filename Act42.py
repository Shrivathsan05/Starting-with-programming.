#Let's create a function total_calc() that helps us calculate and print out the total amount paid at a restaurant. Given a bill amount and the percentage of the bill amount you decide to pay us a tip (tip_perc ), this function calculates the total amount you should pay.
def TotalCalculation(BillAmount, TipPercent) :
    Total = BillAmount * (1 + 0.01 * TipPercent)
    Total = round (Total, 2)
    print (f" Please pay ${Total}! ")
TotalCalculation (150, 20)

