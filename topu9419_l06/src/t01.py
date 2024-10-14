"""
-------------------------------------------------------
TESTING WITH INTEGERS
-------------------------------------------------------
Author:  Ayla Topuz
ID:      169069419
Email:   topu9419@mylaurier.ca
__updated__ = "2024-02-16"
-------------------------------------------------------
"""
from List_linked import List

lst = List()

#append, prepend, insert
lst.append(1)
lst.append(2)
lst.prepend(0)
lst.insert(2, 5)

#list display
print("List:", end=" ")
for item in lst:
    print(item, end=" ")
print()

# Linear search
previous, current, index = lst._linear_search(1)

# Count, max, min
count = lst.count(1)
max_value = lst.max()
min_value = lst.min()

# Find, index, __contains__
value_found = lst.find(1)
index_found = lst.index(1)
contains_1 = 1 in lst

# Peek and remove
first_value = lst.peek()
removed_value = lst.remove(1)

# __getitem__ and __setitem__
first_item = lst[0]
lst[0] = 10

print("Linear search:", previous._value, current._value, index)
print("Count:", count)
print("Max value:", max_value)
print("Min value:", min_value)
print("Value found:", value_found)
print("Index found:", index_found)
print("Contains (1):", contains_1)
print("First value:", first_value)
print("Removed value:", removed_value)
print("Front item :", first_item)
