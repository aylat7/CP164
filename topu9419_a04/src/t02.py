"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ayla Topuz
ID:      169069419
Email:   topu9419@mylaurier.ca
__updated__ = "2024-01-31"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue

target = Queue()

values = [1,2,3,4,5]
for value in values:
    target.insert(value)
    
source = Queue()
values = [1,2,3,3,5]
for value in values:
    source.insert(value)
    
equals = source == target
print(equals)