from typing import Any


def callLimit(limit: int):
    '''Decorator that limits the number of calls to a function'''
    count = 0

    def callLimiter(function):
        '''wrapper function for the decorator'''
        def limit_function(*args: Any, **kwds: Any):
            '''count the number of calls to the function'''
            nonlocal count
            count += 1
            if count > limit:
                print("Error: ", function, " called too many times")
                return
            return function(*args, **kwds)
        return limit_function
    return callLimiter
