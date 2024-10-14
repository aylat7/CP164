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
from Priority_Queue_array import Priority_Queue

source = Priority_Queue()
values = [1,5,3,6,8,4,6,9,5,3,4]
for value in values:
    source.insert(value)
    
key = 5
target1, target2 = source.split_key(key)

print("t1")
for value in target1:
    print(value)
print("t2")
for value in target2:
    print(value)