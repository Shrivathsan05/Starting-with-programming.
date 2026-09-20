import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
Root = Tk("Stationary Order Management App")
Root.geometry("600x300")
Root.title("Stationary Order Management App")
row_totals = {}

class StationaryOrderManagement:
    def __init__(Self, Root):
        Self.root = Root
        Self.root.title("Stationary Order Management App")
        Self.root.geometry("1000x400")
    Items = {"Pen": 20.99, "Notebook": 13.99, "Eraser": 9.99, "Pencil": 18.99, "Marker": 15.99, "Ruler": 12.99}
    CanvasS = Canvas(Root, width=600, height=400)
    CanvasS.pack()
    Frame = ttk.Frame(Root, width=600, height=400)
    Frame.place(x=0, y=0)
    CurrencyDropDownMenu = ttk.Combobox(Frame, values=["USD", "INR"])
    CurrencyDropDownMenu.grid(row=1, column=4, padx=10, pady=10)
    CurrencyDropDownMenu.set(CurrencyDropDownMenu.get())
    if CurrencyDropDownMenu.get() == "USD":
        CurrencyDropDownMenu.set("Currency : USD")
    if CurrencyDropDownMenu.get() == "INR":
        CurrencyDropDownMenu.set("Currency : INR")
    grand_total_row_idx = len(Items) + 3
    ttk.Label(Frame, text="Grand Total:", font=('Arial', 10, 'bold')).grid(row=grand_total_row_idx, column=2, padx=10, pady=15, sticky="e")
    GrandTotalLabel = ttk.Label(Frame, text="$0.00", font=('Arial', 10, 'bold'), anchor="e", width=10)
    GrandTotalLabel.grid(row=grand_total_row_idx, column=3, padx=10, pady=15)

    headers = ["Product Name", "Unit Price", "Quantity (Editable)", "Total Price", "Currency"]
    for col_idx, text in enumerate(headers):
        header_lbl = ttk.Label(Frame, text=text, font=('Arial', 10, 'bold'))
        header_lbl.grid(row=0, column=col_idx, padx=10, pady=5, sticky="w")

    for index,item in enumerate(Items, start=1):
        LabelItem = ttk.Label(Frame, text=f"{item}", width=10, anchor="e")
        LabelItem.grid(row=index, column=0, padx=10, pady=4)  
        LabelUnitPrice = ttk.Label(Frame, text=f"${Items[item]:.2f}", width=10, anchor="e")
        LabelUnitPrice.grid(row=index, column=1, padx=10, pady=4)
        LabelQuantity = ttk.Entry(Frame, width=10,)
        LabelQuantity.grid(row=index, column=2, padx=10, pady=4)
        LabelTotalPrice = ttk.Label(Frame, text="", width=10, anchor="e")
        LabelTotalPrice.grid(row=index, column=3, padx=10, pady=4)
        LabelCurrency = ttk.Label(Frame, text=CurrencyDropDownMenu.get(), width=10, anchor="e")
        LabelCurrency.grid(row=index, column=4, padx=10, pady=4)

        def do_math(event, q=LabelQuantity, p=LabelUnitPrice, t=LabelTotalPrice, c=LabelCurrency, CurrencyDropDownMenu=CurrencyDropDownMenu,item_name=item, GrandTotalLabel=GrandTotalLabel):
            try:
                qty = int(q.get() or 0)
                if CurrencyDropDownMenu.get() == "USD":
                    result = qty * float(p.cget("text").replace("$", ""))
                    t.config(text=f"${result:.2f}")
                if CurrencyDropDownMenu.get() == "INR":
                    result = qty * float(p.cget("text").replace("$", "")) * 95.96
                    t.config(text=f"₹{result:.2f}")
                c.config(text=CurrencyDropDownMenu.get())
                print(result)
                row_totals[item_name] = {"qty": qty, "total": result}
            except ValueError:
                t.config(text="$0.00")
            grand_total = sum(row_totals[item_name]["total"] for item_name in row_totals)
            if CurrencyDropDownMenu.get() == "INR":
                GrandTotalLabel.config(text=f"₹{grand_total:.2f}")
            else:
                GrandTotalLabel.config(text=f"${grand_total:.2f}")
            print("Grand Total:", grand_total)
        LabelQuantity.bind("<KeyRelease>", do_math)
        def show_summary(CurrencyDropDownMenu=CurrencyDropDownMenu, row_totals=row_totals):
            current_currency = CurrencyDropDownMenu.get()
            currency_symbol = "₹" if current_currency == "INR" else "$"
            summary_lines = ["--- ORDER SUMMARY ---"]
            grand_total = 0.0
            for item_name, data in row_totals.items():
                if data["qty"] > 0:
                    summary_lines.append(f"{item_name}: {data['qty']} units — {currency_symbol}{data['total']:.2f}")
                    grand_total += data["total"]
            if len(summary_lines) == 1:
                messagebox.showwarning("Empty Order", "Please enter a quantity for at least one item before ordering.")
                return
            summary_lines.append("\n------------------------")
            summary_lines.append(f"Total Amount Due: {currency_symbol}{grand_total:.2f}")
            full_message = "\n".join(summary_lines)
            messagebox.showinfo("Order Confirmation", full_message)
        OrderButton = ttk.Button(Frame, text="Place Order", command=show_summary)
        OrderButton.grid(row=grand_total_row_idx, column=4, padx=10, pady=15, sticky="e")
Root.mainloop()