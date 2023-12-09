def validate_args(func):
    def wrapper(*args):
        if len(args) != 1:
            return "Not enough arguments" if len(args) < 1 else "Too many arguments"
        
        if not isinstance(args[0], int):
            return "Wrong types"

        if args[0] < 0:
            return "Negative argument"

        return func(*args)

    return wrapper


@validate_args
def my_function(n):
    return f"Argument {n} is valid."

print(my_function(5))       
print(my_function(-2))      
print(my_function(2.5))     
print(my_function(1, 2))     
print(my_function())
