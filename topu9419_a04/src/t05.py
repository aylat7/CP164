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
from functions import pq_split_key
from Priority_Queue_array import Priority_Queue

count = 0
source = Priority_Queue()

key = int(input("Enter object key: "))
length = int(input("Enter list length: "))

while count < length:
    num = int(input("Enter a new num: "))
    source.insert(num)
    count += 1
    
target1, target2 = pq_split_key(source, key)

print("t1")
print(target1._values)
print("t2")
print(target2._values)