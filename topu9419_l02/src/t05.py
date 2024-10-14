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
from utilities import stack_test
from Stack_array import Stack

stack = Stack()

source = open("foods.txt", "r")
stack_test(source)


for i in stack:
    print(i)