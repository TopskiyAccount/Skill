import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time for {func.__name__}: {execution_time:.5f} seconds")
        return result

    return wrapper


def memoize(func):
    cache = {}

    def wrapper(n):
        if n in cache:
            return cache[n]
        result = func(n)
        cache[n] = result
        return result

    return wrapper


def save_info(func):
    def wrapper(n):
        return func(n)

    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__

    return wrapper


def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


@memoize
def fibonacci_memoized(n):
    if n < 2:
        return n
    return fibonacci_memoized(n - 1) + fibonacci_memoized(n - 2)


n = 35
fibonacci_with_timer = timer(fibonacci)
fibonacci_memoized_with_timer = timer(fibonacci_memoized)

fibonacci_with_timer(n)  
fibonacci_memoized_with_timer(n)  
