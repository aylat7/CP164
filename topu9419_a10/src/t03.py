"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ayla Topuz
ID:      169069419
Email:   topu9419@mylaurier.ca
__updated__ = "2024-03-27"
-------------------------------------------------------
"""
from Sorts_array import Sorts

# Create an array with sample data
array = [170, 45, 75, 90, 802, 24, 2, 66]

# Test gnome sort
print("Original Array:")
print(array)
Sorts.gnome_sort(array)
print("Sorted Array:")
print(array)