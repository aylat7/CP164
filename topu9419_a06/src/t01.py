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
from Queue_linked import Queue

queue1 = Queue()
queue2 = Queue()

for i in range(1, 9):  
    queue1.insert(i)

for i in range(9, 21):
    queue2.insert(i)

print(f"Queue1: is_empty: {queue1.is_empty()}")
print(f"Queue2: is_empty: {queue2.is_empty()}")

print(f"Front: Queue1: {queue1.peek()}")
print(f"Front: Queue2: {queue2.peek()}")

print(f"Remove: Queue1: {queue1.remove()}")
print(f"Removed: Queue2: {queue2.remove()}")

queue3 = Queue()

queue3.combine(queue1, queue2)

print("combine Queue1 and Queue2 = Queue3:")
for value in queue3:
    print(value, end=" ")
print()

queue1, queue2 = queue3.split_alt()

print("Queue1 = split Queue3:")
for value in queue1:
    print(value, end=" ")
print()

print("Queue2 = split Queue3:")
for value in queue2:
    print(value, end=" ")
print()

print(f"len: Queue1: {len(queue1)}")
print(f"len: Queue2: {len(queue2)}")

queue1._append_queue(queue2)

print("Queue1 append Queue2:")
for value in queue1:
    print(value, end=" ")
print()
