def memoize(func):
    cache = {}  
    func_name = func.__name__  
    docstring = func.__doc__  

    def wrapper(n):
        if n in cache:
            return cache[n]
        result = func(n)
        cache[n] = result
        return result

    wrapper.__name__ = func_name  
    wrapper.__doc__ = docstring  

    return wrapper

@memoize
def fibonacci(n):
    """
    Calculate the nth Fibonacci number.
    """
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


n = 10
result = fibonacci(n)
print(f"The {n}-th Fibonacci number is: {result}")
