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

from utilities import stack_to_array
from Stack_array import Stack

stack = Stack()


stack.push(69)

target = [6, 3, 7]



stack_to_array(stack, target)

print(target)