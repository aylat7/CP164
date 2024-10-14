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
from Queue_circular import Queue

target = Queue()

empty = target.is_empty()
print(empty)

full = target.is_full()
print(full)

length = len(target)
print(length)

source = Queue(6)
equals = source == target
print(equals)

values = [1,2,3,4,5]
for value in values:
    target.insert(values)

remove = target.remove()
print(remove)