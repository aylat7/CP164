"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ayla Topuz
ID:      169069419
Email:   topu9419@mylaurier.ca
__updated__ = "2024-03-27"
-------------------------------------------------------
"""
from Deque_linked import Deque
from Sorts_Deque_linked import Sorts

def print_deque(deque):
    current = deque._front
    while current is not None:
        print(current._value, end=" ")
        current = current._next
    print()

deque = Deque()
deque.insert_front(5)
deque.insert_front(3)
deque.insert_front(8)
deque.insert_front(2)
deque.insert_front(7)
deque.insert_front(1)

print("Original Deque:")
print_deque(deque)
Sorts.gnome_sort(deque)
print("Sorted Deque:")
print_deque(deque)