"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ayla Topuz
ID:      169069419
Email:   topu9419@mylaurier.ca
__updated__ = "2024-02-17"
-------------------------------------------------------
"""
from Deque_linked import Deque

d = Deque()

d.insert_rear(0)
d.insert_rear(1)
d.insert_rear(2)
d.insert_rear(3)
d.insert_rear(4)

for i in d:
    print(i)
    
d._swap(d._rear._prev,d._front._next)

print()
for i in d:
    print(i)