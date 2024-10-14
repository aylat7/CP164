"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ayla Topuz
ID:      169069419
Email:   topu9419@mylaurier.ca
__updated__ = "2024-01-18"
-------------------------------------------------------
"""
# Imports

from utilities import array_to_stack
from Stack_array import Stack

source = [1, 5, 7, 3]
stack = Stack()

array_to_stack(stack, source)


for i in stack:
    print(i)