# Decorators are a way to dynamically alter the functionality of your functions. So for example, if you wanted to log information when a function is run, you could use a decorator to add this functionality without modifying the source code of your original function. So let's take a look at how these decorators work and a few ways in which we can use them.
# Simply you take 1 function, add some functionality and return the new function without changing the original code.

# Example of Closures
def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function

hi_func = outer_function("Hi")
bye_func = outer_function("Bye")

hi_func()
bye_func()

# Example of Decorator
def decorator_function(original_function):
    # *args and **kwargs are used to pass a variable number of arguments to the function
    def wrapper_function(*args, **kwargs):
        print("Wrapper function executed this before {}".format(original_function.__name__))
        original_function(*args, **kwargs)
    return wrapper_function

# You dont have to use classes instead of functions for the decorator. Just demonstrates that this is an option / alternative method. Function decorators are easier to read and write and are used more often.
class decorator_class(object):
    # use an init method to initialize the decorator class
    # Ties our function with the instance of the class
    def __init__(self, original_function):
        self.original_function = original_function

    # __call__ is a special method that allows an instance of the class to be called as a function
    def __call__(self, *args, **kwargs):
        print("Call method executed this before {}".format(self.original_function.__name__))
        self.original_function(*args, **kwargs)


def display_original():
    print("Display function ran with original syntax")

# More traditional syntax and easier to read
@decorator_function
def display_decorated():
    print("Display function ran with updated syntax")

# Syntax that uses classes for the decorator
@decorator_class
def display_info_1(name, age):
    print("Display info ran with arguments ({}, {})".format(name, age))

# Example 1 - syntax 1
decorated_display = decorator_function(display_original)
decorated_display()

# Example 1 - syntax 2
display_decorated()

# Example 2
# Without *Args and **Kwargs in the wrapper function, the function would throw an error
display_info_1("John", 25)

from functools import wraps

# Practical Example
def my_logger(original_function):
    import logging
    # Create a log file with the name of the function, wrapper function takes in the name of the arguments and the keyword arguments
    # Runs logging.INFO (ran functiosn and logs the arguments)
    logging.basicConfig(filename="{}.log".format(original_function.__name__), level=logging.INFO)

    # Create a wrapper function
    @wraps(original_function)
    def wrapper(*args, **kwargs):
        logging.info(
            "Ran with args: {} and kwargs: {}".format(args, kwargs)
        )
        return original_function(*args, **kwargs)
    return wrapper

def my_timer(original_function):
    import time

    @wraps(original_function)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time()
        print("{} ran in: {} seconds".format(original_function.__name__, t2-t1))
        return result
    return wrapper

# If we don't use functools.wraps in our decorator wrappers, stacking multiple decorators will cause the decorated function's __name__ and other metadata to be replaced by 'wrapper' instead of preserving the original function's information.
@my_timer
@my_logger
def display_info_2(name, age):
    print("display_info_2 ran with arguments ({}, {})".format(name, age))

print(display_info_2.__name__) # Would be wrapper if we didn't use wraps()

display_info_2("Hank", 36)