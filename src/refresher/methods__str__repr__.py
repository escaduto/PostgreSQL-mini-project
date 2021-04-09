# representing objects as strings 

class Person: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age

    # def __str__(self): 
    #     return f"{self.name} is {self.age} years old."

    def __repr__(self):
        return f"<Person({self.name} is {self.age})>"

# magic methods dont need to be called explicitly 
bob = Person("Bob", 35)

print(str(bob))

