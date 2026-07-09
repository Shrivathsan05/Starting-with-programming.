class Library() :
    IsAvailable = True
    def Borrowed(Self) :
        IsAvailable = False
        print(" This book is not available now! ")
    def Available(Self) :
        IsAvailable = True
        print(" This book is available now! ")
    def Borrowing(Self) :
        print(" You are borrowing this book! ")
        IsAvailable = False
        print(" So this book is not available now! ")
    def Returning(Self) :
        print(" You are returning this book! ")
        IsAvailable = True
        print(" So this book is available now! ")
    if IsAvailable == False :
        print(" This book is not available now! ")
    if IsAvailable == True :
        print(" This book is available now! ")
Book1 = Library()
Book2 = Library()
Book3 = Library()
