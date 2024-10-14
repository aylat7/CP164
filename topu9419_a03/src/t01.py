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

from functions import stack_combine
from Stack_array import Stack

source1 = Stack()

source1.push(8)
source1.push(12)
source1.push(8)
source1.push(5)

source2 = Stack()


source2.push(14)
source2.push(9)
source2.push(7)
source2.push(1)
source2.push(6)
source2.push(3)

target = Stack()

target = stack_combine(source1, source2)


for i in target:
    print(i)