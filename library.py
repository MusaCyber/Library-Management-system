class library:
    def __init__(self):
        self.books=[]
        self.no_of_books=0
    def add_book(self):
        b=input("enter book :")
        self.books.append(b)
        self.no_of_books+=1
    def show_books(self):
        for i in self.books:
            print("books :",i)
    def no(self):
         print("No of books Present in a library :",self.no_of_books)
l=library()
print("Welcome to the Library")
n=int(input("How many books you want to add in library :"))
for i in range(n):
    l.add_book()
l.show_books()
l.no()
#if you dont want user to enter instead you enter books manually:
#class Library:
    # def __init__(self):
    #     self.books = []
    #     self.no_of_books = 0

    # def add_book(self, book):   # <-- take book name as argument
    #     self.books.append(book)
    #     self.no_of_books += 1

    # def show_books(self):
    #     for book in self.books:
    #         print("Book:", book)

    # def show_count(self):
    #     print("No of books present in the library:", self.no_of_books)
