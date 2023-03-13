def decorator_function(function):
    def function_return(*args, **kwargs):
        # use args/kwargs if arguments required
        print("accessed decorator function")
        return function
    return function_return()

class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print("accessed decorator class")
        return self.original_function(*args, **kwargs)

@decorator_function
# makes the call of below function to be wrapped with noted decorator function
def other_function(name, age):
    print(f'I am {name} and I am {str(age)}')

# other_function("Eddie", 30)
# removes step of calling decorator function with other function

@decorator_class
# class can also be used as a decorator
def other_function(name, age):
    print(f'I am {name} and I am {str(age)}')

# other_function("eddie", 30)

from functools import wraps
# tool to use same original function when using multiple decorators

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    # denoted to use original function and not nested decorator
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    @wraps(orig_func)
    # denoted to use original function and not nested decorator
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper

import time

@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('Tom', 22)