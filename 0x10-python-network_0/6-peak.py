#!/usr/bin/python3

"""This module finds a peak in a list of unsorted integers.
It uses a modified binary search algorithm to find the peak.
It achieves efficiency by comparing mid with its neighbors to decide the direction of search
"""

def find_peak(list_of_integers):
    """This function finds a peak in a list of unsorted integers"""
    if not list_of_integers:
        return None

    left = 0
    right = len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return list_of_integers[left]
