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
# Imports

from Stack_array import Stack

source1 = Stack()

source1.push(2)
source1.push(3)
source1.push(4)
source1.push(5)
source1.push(6)

source2 = Stack()

source2.push(7)
source2.push(8)
source2.push(9)
source2.push(10)
source2.push(11)

target = Stack()

target.combine(source1, source2)

for i in target:
    print(i)