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
from Priority_Queue_linked import Priority_Queue

pq1 = Priority_Queue()
pq2 = Priority_Queue()

for value in [6, 2, 7, 6, 1]:
    pq1.insert(value)

for value in [6, 9, 6, 0, 5]:
    pq2.insert(value)

print("Rrmoved value in pq1:", pq1.remove())

print("peeked value in pq1:", pq1.peek())

print("pq1 is_empty", pq1.is_empty())

print("len pq1:", len(pq1))

target1, target2 = pq2.split_alt()
print("target1; split_alt:", list(target1))
print("target2; split_alt:", list(target2))

for value in [22, 5, 8, 1, 9]:
    pq2.insert(value)

key = 5
target3, target4 = pq2.split_key(key)
print("target3; split_key, key = 5:", list(target3))
print("target4; split_key, key = 5:", list(target4))

combined_pq = Priority_Queue()
combined_pq.combine(pq1, target4)
print("combined_pq; pq1, target4:", list(combined_pq))
