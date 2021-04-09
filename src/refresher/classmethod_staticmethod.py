# creating class methods and static method 

class ClassTest: 
    def instance_method(self): 
        print(f'called instance_method of {self}')

    @classmethod
    def class_method(cls): 
        print(f'called class_method of {cls}')

    @staticmethod 
    def static_method():
        print('called static_method')




test = ClassTest()

ClassTest.instance_method(test) # produce action that uses the object created, to modify data in self 
ClassTest.class_method() # used as factories 
ClassTest.static_method() # separate function that lives inside class, place a method inside a class for code organization etc. 


# class method example: 

class Book: 
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight): 
        self.name = name 
        self.book_type = book_type
        self.weight = weight 

    def __repr__(self):
        return f'<Book {self.name}, {self.book_type}, weighing {self.weight}g>'


    @ classmethod
    def hardcover(cls, name, page_weight) -> "Book": 
        return cls(name, cls.TYPES[0], page_weight + 100)

    @ classmethod
    def hardcover(cls, name, page_weight)-> "Book": 
        return cls(name, cls.TYPES[1], page_weight)


print(Book.TYPES)
book = Book.hardcover("Harry Potter", 1500)
light =  Book.hardcover("Python 101", 600)
print(book)
print(light)

