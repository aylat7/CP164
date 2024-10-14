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
from Sorted_List_linked import Sorted_List

# Test data
data = [170, 45, 75, 90, 802, 24, 2, 66]

# Display original data
print("Original list:")
print(data)

# Apply radix sort
Sorted_List.radix_sort(data)

# Display sorted data
print("Sorted list:")
print(data)