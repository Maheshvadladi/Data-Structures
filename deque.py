'''
deque

appendleft()
1->2 3 4 5 6

delete:
pop()
2 3 4 5 (5)

popleft()
(2) 3 4 5

utility:
clear() - empty the queue
copy() - creates a copy of queue
count() - count occurences
index() - give the index value

extend methods:
extend([1 2 3])
extendleft([4,5]) 4 5 1 2 3

default
reverse()
rotate()
'''

# operations in deque
from collections import deque
dq = deque()
n = int(input("Enter the size of queue: "))
for i in range(n):
    val = int(input("Enter value: "))
    dq.append(val)
print("Deque after input: ", dq)
x = int(input("Enter value to insert at left: "))
dq.appendleft(x)
print("Deque after append left: ", dq)
r = int(input("Enter value to insert at right: "))
dq.append(r)
print("Deque after append right: ", dq)
dq.popleft()
print("Deque after delete left: ", dq)
dq.pop()
print("Deque after delete right: ", dq)
dq.reverse()
print("Reverse: ", dq)
k = int(input("Enter k value to be rotated: "))
dq.rotate()
print("Rotate: ", dq)