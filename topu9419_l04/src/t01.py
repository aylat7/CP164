"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ayla Topuz
ID:      169069419
Email:   topu9419@mylaurier.ca
__updated__ = "2024-01-30"
-------------------------------------------------------
"""
from List_array import List
from utilities import list_test

target = List()

source = open("foods.txt", "r")
list_test(source)

for i in target:
    print(i)



