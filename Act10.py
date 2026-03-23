#Write to check if a person is buying oranges at 100 rs and later selling it 1at 120 rs. Find that he has profit or loss?
Actual_Cost = float(input("Please enter the actual product price: "))
Sale_Amount = float(input("Please enter the sales amount: "))

if (Sale_Amount > Actual_Cost):
    Amount = Sale_Amount - Actual_Cost
    print("Total Profit = {0}".format(Amount))

else:
    print("No Profit!")


