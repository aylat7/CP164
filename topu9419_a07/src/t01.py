"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ayla Topuz
ID:      169069419
Email:   topu9419@mylaurier.ca
__updated__ = "2024-03-10"
-------------------------------------------------------
"""
from List_linked import List

new_list1 = List()
new_list2 = List()
source = List()
target = List()
new_target1 = List()
new_target2 = List()
new_target3 = List()
source1 = List()
source2 = List()
printed_list1 = []
printed_list2 = []
printed_list3 = []

print()
print("__eq__ test: ")
print("-----------------------------")
avacado = int(input("Enter length of list: "))
count = 0
while count < avacado:
    val = int(input("Enter a value: "))
    source.append(val)
    count += 1
printed_list2 = []
for x in source:
    printed_list2.append(x)
print(printed_list2)

print()
print("__getitem__ test: ")
print("-----------------------------")
print(printed_list1)
beans = int(input("Enter index to get in list: "))
value = new_list1[beans]
print(value)

print()
print("clean test: ")
print("-----------------------------")
print(printed_list1)
new_list1.clean()
printed_list1 = []
for x in new_list1:
    printed_list1.append(x)
print(printed_list1)

print()
print("combine test: ")
print("-----------------------------")
cheese = int(input("Enter length of list: "))
count = 0
while count < cheese:
    val = int(input("Enter a value: "))
    source.inset(val)
    count += 1
printed_list2 = []
for x in source1:
    printed_list2.append(x)
print(printed_list2)

salsa = int(input("Enter length of list: "))
count = 0
while count < salsa:
    val = int(input("Enter a value: "))
    source.inset(val)
    count += 1
printed_list2 = []
for x in source2:
    printed_list2.append(x)
print(printed_list2)

print()
print("Intersection test: ")
print("-----------------------------")
i = int(input("Emter len of list: "))
hate = 0
while hate < i:
    cs = int(input("Enter a value: "))
    source1.insert(cs)
    count += 1
printed_list2 = []
for x in source1:
    printed_list2.append(x)
print(printed_list2)

i = int(input("Enter len of list: "))
cs = 0 
while cs < i:
    value = int(input("Emter a value: "))
    source2.insert(value)
    count += 1
printed_list2 = []
for x in source2:
    printed_list2.append(x)
print(printed_list2)

new_target2.intersection(source1, source2)
printed_list1 = []
for x in new_target2:
    printed_list1.append(x)
print(printed_list1)

print()
print("union test: ")
print("---------------------------------")
new_target3 = List()
source1 = List()
source2 =List()

length = int(input("Enter length of list: "))
count = 0
while count< length:
    value = int(input("Enter a value: "))
    source1.insert(value)
    count += 1
printed_list2 = []
for x in source1:
    printed_list2.append(x)
print(printed_list2)

length = int(input("Enter length of listt: "))
count = 0
while count < length:
    value = int(input("Enter a val: "))
    source2.insert(value)
    count += 1
printed_list2 = []
for x in source2:
    printed_list2.append(x)
print(printed_list2)

new_target3.union(source1, source2)
printed_list1 = []
for x in new_target3:
    printed_list1.append(x)
print(printed_list1)

print()
print("Remove_front test: ")
print("---------------------------------")
new_list1.remove_front()
printed_list1 = []
for x in new_list2:
    printed_list1.append(x)
print(printed_list1)