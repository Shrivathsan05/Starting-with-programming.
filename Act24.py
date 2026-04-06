#Write a program to calculate the electricity bill. The bill is calculated by checking the number of units consumed. Suppose the user is consuming less than 50 units. The per-unit cost will be 2.60, and the tax on that bill will be 25. If a user is consuming more than 50 but less than 100. Then the per-unit cost will be 3.25, and the tax on that bill will be 35 If the user is coming more than 100 and less than 200. Then the per-unit cost will be 5.26, and the tax will be 45 And above 200, the cost of the unit is 8.45, and the tax is 75.
Units = int ( input ( " Please enter the amount of units you consumed : ") )
if ( Units < 50 ) : 
    Amount = Units * 2.60
    Surcharge = 25
elif ( Units <= 100 ) : 
    Amount = 130 + ( ( Units - 50 ) * 3.25 )
    Surcharge = 35
elif ( Units <= 200 ) : 
    Amount = 130 + 162.50 + ( ( Units - 100 ) * 5.26 )
    Surcharge = 45
else : 
    Amount = 130 + 162.50 + 526 + ( ( Units - 200 ) * 8.45 )
    Surcharge = 75
Total = Amount + Surcharge 
print ( " \n Electricity Bill = %.2F "  % Total )