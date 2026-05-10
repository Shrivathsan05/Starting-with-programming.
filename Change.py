def Change(P, TB) : 
    return (P - TB) 
Paid = int ( input ( " How many $ (Any type of currency) did you pay? " ) )
TotalBill = int ( input ( " How many $ (Any type of currency) are you supposed to pay according to the bill? " ) )
print (" The amount of $ (Any type of currency) that has to paid back to you as change is,", Change (Paid, TotalBill),"$ (Any type of currency)! ")