#!/usr/bin/python3

"""This module finds a peak in a list of unsorted integers.
It uses a binary search algorithm to find the peak.
"""

def find_peak(list_of_integers):
    """This function finds a peak in a list of unsorted integers"""
    if not list_of_integers:
        return None

    low = 0
    high = len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            high = mid
        else:
            low = mid + 1

    return list_of_integers[low]
