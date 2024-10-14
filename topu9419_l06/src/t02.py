"""
-------------------------------------------------------
TESTING WITH FILE
-------------------------------------------------------
Author:  Ayla Topuz
ID:      169069419
Email:   topu9419@mylaurier.ca
__updated__ = "2024-02-16"
-------------------------------------------------------
"""
from List_linked import List


lst = List()

values = open("foods.txt", "r") 

for value in values:
    lst.append(value)

#append, prepend, insert
lst.append("Beef with Green Pepper|1|False|251")
lst.append("Poutine|0|False|710")
lst.prepend("Teriyaki|6|False|233")
lst.insert(0, "Canada Goose Chili|0|False|199")

#list display
print("List:", end=" ")
for item in lst:
    print(item, end=" ")
print()

# Linear search
print("Linear Search:")
previous, current, index = lst._linear_search("Teriyaki6|False|233")
if previous is not None:
    print("Previous node value:", previous._value)
else:
    print("Previous node not found")

if current is not None:
    print("Current node value:", current._value)
else:
    print("Current node not found")

print("Index:", index)


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

print("Count:", count)
print("Max value:", max_value)
print("Min value:", min_value)
print("Value found:", value_found)
print("Index found:", index_found)
print("Contains (1):", contains_1)
print("First value:", first_value)
print("Removed value:", removed_value)
print("Front item :", first_item)
