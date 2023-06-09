#!/usr/bin/python3
def max_integer(my_list=[]):
    """Find the largest integer."""
    if len(my_list) == 0:
        return (None)

    b = my_list[0]
    for n in range(len(my_list)):
        if my_list[n] > b:
            b = my_list[n]
    return (b)
