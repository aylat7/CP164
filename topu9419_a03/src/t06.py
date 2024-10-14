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
from functions import postfix
from Stack_array import Stack

string = "4 5 + 12 * 2 3 * -"

answer = Stack()
answer = postfix(string)

print(answer)