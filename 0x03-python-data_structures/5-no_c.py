#!/usr/bin/python3
def no_c(my_string):
    """Remove all characters both c and C from a string."""
    cy = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(cy))
