"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ayla Topuz
ID:      169069419
Email:   topu9419@mylaurier.ca
__updated__ = "2024-01-25"
-------------------------------------------------------
"""
# Imports

from functions import is_palindrome_stack
from Stack_array import Stack

string = "racecar"

palindrome = Stack()
palindrome = is_palindrome_stack(string)

print(palindrome)

