#!/usr/bin/python3
"""
script for finding peak in list of ints, interview prep
"""

"""
Initialize Variables: We start by initializing two pointers, left and right, to represent the range of elements in the list we are currently considering. Initially, left is set to 0, and right is set to the index of the last element in the list.We enter a loop where we repeatedly divide the current range of elements (defined by left and right) in half. We calculate the middle index, mid, as (left + right) // 2.We compare the element at index mid with its adjacent elements, which are mid-1 and mid+1. We repeat the binary search process until left is less than or equal to right. At this point, we have narrowed down the search range to a single element, which is the peak, and we return this element."""

def find_peak(list_of_integers):
    if not list_of_integers:
        return None

    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return list_of_integers[left]
