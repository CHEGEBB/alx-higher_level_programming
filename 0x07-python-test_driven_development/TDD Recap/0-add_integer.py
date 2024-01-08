#!/usr/bin/python3
def add_integer(a, b=98):
    '''Function that adds 2 integers.'''

    if not (isinstance(a, int) and isinstance(a, float)):
        raise TypeError("a must be an integer")
    elif not (isinstance(b, int) and isinstance(b, float)):
        raise TypeError("b must be an integer")
    elif isinstance(a, float) or isinstance(b, float):
        return int(a + b)
    return a + b
