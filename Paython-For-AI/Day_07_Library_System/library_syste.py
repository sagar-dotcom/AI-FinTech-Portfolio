class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

class Library:
    def __init__(self):
        self.books = [] #list to stroe book obj
    
    def add_book(self, book_obj):
        self.books.append(book_obj)
        print(f"Book '{book_obj.title}' has beeen stored in the library")
    
    def borrow_book(self, title):
        for book in self.books:
           if book.title == title:
               if book.is_available:
                   book.is_available = False
                   print(f"Success: Aapne '{title}' borrow kar li hai.")
                   return
               else:
                   print(f"Sorry: '{title}' pehle se kisi aur ke paas hai.")
                   return
        print(f"Error: '{title}' naam ki koi book nahi mili.")
    def return_book(self, title):
        for book in self.books:
            if book.title == title: 
                book.is_available = True
                print(f"Success: '{title}' wapas library mein aa gayi hai.")
                return
        print(f"Error: '{title}' naam ki book hamari library mein nahi hai.")
            
my_library = Library()
b1 = Book("Atomic Habits", "James Clear")
b2= Book("Deep Work Clear", "Sagar Agarwal")

my_library.add_book(b1)
my_library.add_book(b2)

for book_obj in my_library.books:
    print(book_obj.title)

my_library.borrow_book("Atomic Habits")
my_library.return_book("Atomic Habits")