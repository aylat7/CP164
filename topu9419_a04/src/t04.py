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

source = Queue()
values = [1,2,3,4,5]
for value in values:
    source._values.append(value)

target1, target2 = source.split_alt()

print("target1:")
print(target1._values)

print("target2:")
print(target2._values)
