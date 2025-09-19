import time

# 2. Uppercase decorator
def uppercase_decorator(func):  # decorator function
    def wrapper(*args, **kwargs):   # Inner function
        result = func(*args, **kwargs)  # calling the original function
        return result.upper()   # convert output to uppercase
    return wrapper

# 3. Function that returns a greeting
# @uppercase_decorator
def say_hello(name):
    return f"Hello, {name}"

# 4. Appling uppercase_decorator
greet = uppercase_decorator(say_hello)  # Applying decorator to say_hello

# 5. Testing the decorated function
print(greet("Deb"))   # Output will be in uppercase


# 5. Timing decorator
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.6f} seconds")
        return result
    return wrapper


def test_function():
    total = 0
    for i in range(10000):
        total += 1
    return total

# 6. Apply timing_decorator on greet
timed_function = timing_decorator(test_function)

print("\nTesting timed_function:")
print('The output of main function:  ',timed_function())


# 7. Greet function with timing_decorator
timed_greet = timing_decorator(say_hello)

# 8. Testing timed_greet
print("\nTesting timed_greet:")
print(timed_greet("Alice"))


# 9. Math class with add and subtract
class Math:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b
    
# 10. Define a decorator to log method calls
def logging_decorator(func):
    def wrapper(*args, **kwargs):   # Inner function to log the arguments and return value
        print(f"Calling method: {func.__name__} with arguments: {args[1:]}, {kwargs}")  # args[1:] to skip 'self'
        result = func(*args, **kwargs)
        print(f"Method {func.__name__} returned: {result}")
        return result
    return wrapper

# 11. Apply logging_decorator to Math methods
Math.add = logging_decorator(Math.add)
Math.subtract = logging_decorator(Math.subtract)

# 12. Testing Math class with logging_decorator
print("\nTesting Math class with logging_decorator:")
math = Math()
print('\nThe Original Output',math.add(10, 5))
print('\nThe Original Output',math.subtract(20, 8))
