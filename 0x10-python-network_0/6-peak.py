#!/usr/bin/python3

"""This module finds peaks in a list of unsorted integers.
It uses a recursive binary search algorithm to find the peak.
It achieves efficiency by dividing the list in half and
searching the half that contains the greater of the two
"""

def find_peak(list_of_integers):
    """This function finds peaks in a list of unsorted integers"""
    if not list_of_integers:
        return None

    mid = len(list_of_integers) // 2
    peak = list_of_integers[mid]

    # Check if peak is greater than its neighbors
    if (mid == 0 or peak >= list_of_integers[mid - 1]) and \
       (mid == len(list_of_integers) - 1 or peak >= list_of_integers[mid + 1]):
        return peak

    # Recursively search the left half if peak is less than its left neighbor
    if mid > 0 and peak < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])

    # Recursively search the right half if peak is less than its right neighbor
    return find_peak(list_of_integers[mid + 1:])
