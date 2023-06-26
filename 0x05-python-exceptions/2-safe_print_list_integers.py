#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    n = 0
    p = 0
    for n in range(0, x):
        try:
            print("{:d}".format(my_list[n]), end="")
            p += 1
        except (ValueError, TypeError):
            continue
    print()
    return p
