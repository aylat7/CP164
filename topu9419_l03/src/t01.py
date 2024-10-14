"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ayla Topuz
ID:      169069419
Email:   topu9419@mylaurier.ca
__updated__ = "2024-01-24"
-------------------------------------------------------
"""
# Imports
from utilities import priority_queue_test
from Queue_array import Queue

queue = Queue()

a = open("foods.txt", "r")
priority_queue_test(a)

for i in queue:
    print(i)