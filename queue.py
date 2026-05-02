#Enqueue operation
'''queue = []
n = int(input("Enter the size of queue:"))
for i in range(n):
    val = int(input("Enter the value:"))
    queue.append(val)
print("Queue after Enqueue:", queue)'''

#Dequeue operation
'''queue = list(map(int, input("Enter elements:").split()))
if len(queue) == 0:
    print("Queue is empty -Underflow")
else:
    removed = queue.pop(0)
    print("Dequeue element:", removed)
    print("Remaining elements:", queue)
    print("Peek element:", queue[0])
    print("Size of the queue:", len(queue))'''

# enqueue using linked list
'''class node:
    def __init__(self, data):
        self.data = data
        self.next = None
front = rear = None
n = int(input("Enter the size of queue:"))
for i in range(n):
    val = int(input("Enter the value:"))
    new = node(val)
    if front is None:
        front = rear = new
    else:
        rear.next = new
temp = front
print("Queue after enqueue:", end=" ")
while temp:
    print(temp.data, end=" ")
    temp = temp.next'''

# dequeue using linked list
'''class node:
    def __init__(self, data):
        self.data = data
        self.next = None
front = rear = None
n = int(input("Enter the size of queue:"))
for i in range(n):
    val = int(input("Enter the value:"))
    new = node(val)
    if front is None:
        front = rear = new
    else:
        rear.next = new
        rear = new
if front is None:
    print("Queue Empty / Underflow !!!")
else:
    removed = front.data
    front = front.next
    if front is None:
        rear = None
    print("Dequeue element:", removed)
temp = front
print("Queue after Dequeue:", end=" ")
while temp:
    print(temp.data, end=" ")
    temp = temp.next'''

# peek element in queue using linked list
'''class node:
    def __init__(self, data):
        self.data = data
        self.next = None
front = rear = None
n = int(input("Enter the size of queue:"))
for i in range(n):
    val = int(input("Enter the value:"))
    new = node(val)
    if front is None:
        front = rear = new
    else:
        rear.next = new
        rear = new
if front is None:
    print("Queue Empty / Underflow !!!")
else:
    print("Front Element: ", front.data)'''

# count size of dequeue using linked list
'''class node:
    def __init__(self, data):
        self.data = data
        self.next = None
front = rear = None
n = int(input("Enter the size of queue:"))
count = 0
for i in range(n):
    val = int(input("Enter the value:"))
    new = node(val)
    count += 1
    if front is None:
        front = rear = new
    else:
        rear.next = new
        rear = new
print("Size of queue:", count)'''

