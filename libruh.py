
class book():
    def __init__(self, name,author,dop,price):
        self.bookName = name
        self.bookAuthor = author
        self.bookDop = dop
        self.bookPrice = price
    
    def add_book(self):
        print("name: "+self.bookName)
        print("author: "+str(self.bookAuthor))
        print("dop: "+str(self.bookDop))
        print("price: "+self.bookPrice)
        print("book added")
        
    def years_since(self):
        years = 2023 - self.bookDop
        print("this book was published "+str(years)+" years ago")
        print("-----")


book1 = book("el velero", "alexander cruz", 2020, "100$")
book1.add_book()
book1.years_since()