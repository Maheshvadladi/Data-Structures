# operations
# Delete operation

'''class node:
    def __init__(self, data):
        self.data = data
        self.next = None
head = None
def insert(data):
    global head
    newnode = node(data)
    newnode.next = head
    head = newnode
def delete(value):
    global head
    temp = head
    if temp and temp.data == value:
        head = temp.next
        return 
    prev = None
    while temp and temp.data != value:
        prev = temp
        temp = temp.next
    if temp is None:
        print("Value not in LinkedList......😊")
        return
    prev.next = temp.next
    print("Deleted value:", value)
def display():
    temp = head
    while temp:
        print(temp.data, end="->")
        temp = temp.next
    print("None")

n = int(input("Enter the number of nodes:"))
for _ in range(n):
    val = int(input("Enter the value:"))
    insert(val)
print("Inserted Linkedlist:")
display()
key = int(input("Enter the value of node to be deleted:"))
delete(key)
print("\n Updated Linkedlist:")
display()'''

#Search operation

'''class node:
    def __init__(self, data):
        self.data = data
        self.next = None
head = None
def insert(data):
    global head
    newnode = node(data)
    newnode.next = head
    head = newnode
def search(key):
    temp = head
    position = 1
    while temp:
        if temp.data == key:
            print("Element found in node:", position)
            return
        temp = temp.next
        position += 1
    print("No node reflects the key ....")
def display():
    temp = head
    while temp:
        print(temp.data, end="->")
        temp = temp.next
    print("None")

n = int(input("Enter the number of nodes:"))
for _ in range(n):
    val = int(input("Enter the value:"))
    insert(val)
print("Inserted Linkedlist:")
display()
key = int(input("Enter the value of node to be searched:"))
search(key)'''

# Reverse operation

'''class node:
    def __init__(self, data):
        self.data = data
        self.next = None
head = None
def insert(data):
    global head
    newnode = node(data)
    newnode.next = head
    head = newnode
def reverse():
    global head
    prev = None
    curr = head
    while curr:
        nextnode = curr.next
        curr.next = prev
        prev = curr
        curr = nextnode
    head = prev
    print("Reverse Linkedlist:")
def display():
    temp = head
    while temp:
        print(temp.data, end="->")
        temp = temp.next
    print("None")

n = int(input("Enter the number of nodes:"))
for _ in range(n):
    val = int(input("Enter the value:"))
    insert(val)
print("Inserted Linkedlist:")
display()
reverse()
display()'''

#replace element in a singly linked list

'''class node:
    def __init__(self, data):
        self.data = data
        self.next = None
head = None
def insert(data):
    global head
    newnode = node(data)
    newnode.next = head
    head = newnode

def display():
    temp = head
    while temp:
        print(temp.data, end="->")
        temp = temp.next
    print("None")
def replace(old, new):
    temp = head
    found = False
    while temp:
        if temp.data == old:
            temp.data = new
            found = True
        temp = temp.next
    if found:
        print("Replaced", old, "with", new)
    else:
        print("Value is not found in SLL")
n = int(input("Enter the number of nodes:"))
for _ in range(n):
    val = int(input("Enter the value:"))
    insert(val)
print("Inserted Linkedlist:")
display()
old = int(input("Enter value to replace:"))
new = int(input("Enter new value:"))
replace(old, new)
print("\n Updated Linkedlist:")
display()'''

