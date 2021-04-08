'''
unpacking arguments
'''

def multiply(*args):
    '''
    astericks allows user to input multiple parameters into argument.
    '''
    print(args)
    total = 1 
    for arg in args:
        total = total * arg

    return total

def apply(*args, operator):
    '''
    function that takes in multiple arguments and performs either 
    multiplication and/or addition. 
    '''
    if operator == "*":
        return multiply(*args) 
    elif operator == "+":
        return sum(args) 
    else: 
        return "No valid operator provided to apply()."
    

print(apply(1, 3, 5), operator="*")
