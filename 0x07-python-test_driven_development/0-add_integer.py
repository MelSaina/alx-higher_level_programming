#!/usr/bin/python3
def add_integer(a, b=98):
    """Adds 2 integers.
    Args:
        a (int or float): The first integer to add.
        b (int or float): The second integer to add. Defaults to 98.
    Returns:
        int: The sum of a and b.
    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
