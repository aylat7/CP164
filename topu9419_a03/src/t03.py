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
from functions import stack_reverse
from Stack_array import Stack


source = Stack()

source.push(2)
source.push(3)
source.push(4)
source.push(5)
source.push(6)
    
    

stack_reverse(source)

for i in source._values:
    print(i)