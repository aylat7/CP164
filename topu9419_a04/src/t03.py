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
from functions import queue_split_alt

source = Queue()

values = [1,2,3,4,5]
for value in values:
    source.insert(value)

target1, target2 = queue_split_alt(source)

print("Target 1:")
for item in target1:
    print(item)
    
print("Target 2:")
for item in target2:
    print(item)