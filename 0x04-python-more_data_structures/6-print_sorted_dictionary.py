#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for ky in sorted(a_dictionary):
        val = a_dictionary.get(ky)
        print('{}: {}'.format(ky, val))
