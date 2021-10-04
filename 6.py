### Task 4.6
# Implement a decorator `call_once` which runs a
# function or method once and caches the result.
# All consecutive calls to this function should
# return cached result no matter the arguments.


def call_once(func):
    cache = None

    def wrapper(*args):
        nonlocal cache
        if cache == None:
            cache = func(*args)
        return cache
    return wrapper



@call_once
def sum_of_numbers(a, b):
    return a + b

print(sum_of_numbers(2, 6))
print(sum_of_numbers(8, 7))