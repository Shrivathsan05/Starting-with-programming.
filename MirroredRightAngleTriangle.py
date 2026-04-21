Rows = int(input("Enter the Number of Rows: "))
for i in range(1, Rows + 1):
    print("  " * (Rows - i), end="")
    print("* " * i,"* " * i )

