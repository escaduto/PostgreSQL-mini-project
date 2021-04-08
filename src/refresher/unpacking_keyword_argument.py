def named(name, age): 
    print(name, age)

details = {"name":'Bob', 'age':25}

# pass in multiple keywords arguments with ** 
named(**details)

def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")

print_nicely(name="Bob", age=25)


# positional arguments in args; named arguments are kwargs
def both(*args, **kwargs):
    print(args) 
    print(kwargs)

both(1, 3, 5, name="Bob", age=25)
