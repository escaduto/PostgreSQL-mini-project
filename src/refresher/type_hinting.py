from typing import List 

def list_avg(sequence: List) -> float: 
    return sum(sequence) / len(sequence) 

list_avg([123, 23, 12])

class Book:
    def __init__(self, name):
        self.name = name 

class BookShelf: 
    def __init__(self, books: List[Book]):
        self.books = books 

    def __str__(self) -> str: 
        return f"Bookshelf with {len(self.books)} books."

book = Book("Harry Potter")
book2 = Book("Python 101")
book3 = Book("Python 102")
book4 = Book("Python 105")

shelf = BookShelf([book, book2, book3, book4])

print(shelf)