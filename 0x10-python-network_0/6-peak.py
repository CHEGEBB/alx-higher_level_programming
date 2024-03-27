#!/usr/bin/python3

"""This module finds a peak in a list of unsorted integers.
It uses a recursive binary search algorithm to find the peak.
It achieves efficiency by dividing the list in half and
searching the half that contains the greater of the two
"""
def find_peak(list_of_integers):
    """This function finds a peak in a list of unsorted integers"""
    if not list_of_integers:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if len(list_of_integers) == 2:
        return max(list_of_integers)
    mid = len(list_of_integers) // 2
    if list_of_integers[mid] > list_of_integers[mid - 1] and \
       list_of_integers[mid] > list_of_integers[mid + 1]:
        return list_of_integers[mid]
    if list_of_integers[mid + 1] > list_of_integers[mid]:
        return find_peak(list_of_integers[mid + 1:])
    return find_peak(list_of_integers[:mid])
