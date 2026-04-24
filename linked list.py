#Linked list inserting from tail
'''class node:
    def __init__(self,data):
        self.data = data
        self.next = None
n = int(input("Enter the number of nodes:"))
head = None
for i in range(n):
    val = int(input("Enter the value:"))
    newnode = node(val)
    if head is None:
        head = newnode
    else:
        temp = head
        while temp.next:
            temp = temp.next
        temp.next = newnode
print("Linked List:", end=" ")
temp = head
while temp:
    print(temp.data, end=" ")
    temp = temp.next
print("None")'''

#Linked list inserting from head only one element
'''class node:
    def __init__(self,data):
        self.data = data
        self.next = None
n = int(input("Enter the number of nodes:"))
head = None
for i in range(n):
    val = int(input("Enter the value:"))
    newnode = node(val)
    if head is None:
        head = newnode
    else:
        temp = head
        while temp.next:
            temp = temp.next
        temp.next = newnode
x = int(input("Enter values to insert at begining:"))
newnode = node(x)
newnode.next = head
head = newnode
print("Linked List:", end=" ")
temp = head
while temp:
    print(temp.data, end="->")
    temp = temp.next
print("None")'''

# Insert all the data from begining in a single linked list

'''class node:
    def __init__(self, data):
        self.data = data
        self.next = None
head = None
def insertbegin(data):
    global head
    newnode = node(data)
    newnode.next = head
    head = newnode

n = int(input("Enter number of nodes:"))
for _ in range(n):
    val = int(input("Enter value:"))
    insertbegin(val)
temp = head
print("Linked List:")
while temp:
    print(temp.data,end = "->")
    temp = temp.next
print("Tail")'''

# insert at begining at DLL

'''class node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
def insert_begin(head, data):
    newnode = node(data)
    if head:
        head.prev = newnode
        newnode.next = head
    return newnode
def display(head):
    temp = head
    while temp:
        print(temp.data, end="->")
        temp = temp.next
    print("None")
head = None
n = int(input("Enter number of nodes:"))
for _ in range(n):
    val = int(input("Enter value:"))
    head = insert_begin(head,val)
display(head)'''

# insert at end in DLL

'''class node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
def insert_end(head, data):
    newnode = node(data)
    if head is None:
        return newnode
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = newnode
    newnode.prev = temp
    return head
def display(head):
    temp = head
    while temp:
        print(temp.data, end="->")
        temp = temp.next
    print("None")
head = None
n = int(input("Enter number of nodes:"))
for _ in range(n):
    val = int(input("Enter value:"))
    head = insert_end(head,val)
display(head)'''

# insert at a disired position in DLL

'''class node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
def insert_pos(head, data, pos):
    newnode = node(data)
    if pos == 1:
        if head:
            head.prev = newnode
            newnode.next = head
            return newnode
        temp = head
        for _ in range(pos-2):
            if temp is None:
                return head
            temp = temp.next
        if temp is None:
            return head
        newnode.next = temp.next
        if temp.next:
            temp.next.prev = newnode
        temp.next = newnode
        newnode.prev = temp
        return head
def display(head):
    temp = head
    while temp:
        print(temp.data, end="->")
        temp = temp.next
    print("None")
head = None
n = int(input("Enter number of nodes:"))
for _ in range(n):
    val = int(input("Enter value:"))
    head = insert_pos(head, val, _-1)
pos = int(input("Enter position to enter:"))
val = int(input("enter value:"))
head = insert_pos(head, val, pos)
display(head)'''

# insert at begining and delete from begining at DLL
'''class node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
def delete_begin(head):
    if head is None:
        return None
    head = head.next
    if head:
        head.prev = None
    return head
def display(head):
    temp = head
    while temp:
        print(temp.data, end="->")
        temp = temp.next
    print("None")
head = None
n = int(input("Enter number of nodes:"))
for _ in range(n):
    val = int(input("Enter value:"))
    new = node(val)
    new.next = head
    if head:
        head.prev = new
    head = new
display(head)
head = delete_begin(head)
display(head)'''

# insert at begining and delete at end in DLL

'''class node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
def delete_end(head):
    if head is None:
        return None
    temp = head
    if temp.next is None:
        return None
    while temp.next:
        temp = temp.next
    temp.prev.next = None
    return head
def display(head):
    temp = head
    while temp:
        print(temp.data, end="->")
        temp = temp.next
    print("None")
head = None
n = int(input("Enter number of nodes:"))
for _ in range(n):
    val = int(input("Enter value:"))
    new = node(val)
    new.next = head
    if head:
        head.prev = new
    head = new
display(head)
head = delete_end(head)
display(head)'''

# Delete by value in DLL

'''class node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
def delete_value(head, key):
    temp = head
    while temp:
        if temp.data == key:
            if temp.prev == None:
                head = temp.next
                if head:
                    head.prev = None
                return head
            if temp.next == None:
                temp.prev.next = None
                return head
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
        temp = temp.next
    return head
def display(head):
    temp = head
    while temp:
        print(temp.data, end="<->")
        temp = temp.next
head=None
n = int(input("Enter the number of nodes:"))
for _ in range(n):
    val = int(input("Enter the value:"))
    if head is None:
        head = node(val)
    else:
        temp = head
        while temp.next:
            temp = temp.next
        new = node(val)
        temp.next = new
        new.prev = temp
key = int(input("Enter the value your want to delete:"))
head = delete_value(head,key)
display(head)'''

# search a value in DLL

'''class node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
def search(head, key):
    temp = head
    pos = 1
    while temp:
        if temp.data == key:
            return pos
        temp = temp.next
        pos += 1
    return -1
head=None
n = int(input("Enter the number of nodes:"))
for _ in range(n):
    val = int(input("Enter the value:"))
    if head is None:
        head = node(val)
    else:
        temp = head
        while temp.next:
            temp = temp.next
        new = node(val)
        temp.next = new
        new.prev = temp
key = int(input("Enter the value your want to search:"))
pos = search(head,key)
if pos != -1:
    print(key, "found at Node:", pos)
else:
    print("Not found")'''

#circular linked list insert at begin
'''class node:
    def __init__(self,data):
        self.data = data
        self.next = None
def insert_begin(head, data):
    new = node(data)
    if head is None:
        new.next = new
        return new
    temp = head
    while temp.next != head:
        temp = temp.next
    new.next = head
    temp.next = new
    head = new
    return head
def display(head):
    if head is None:
        return
    temp = head
    while True:
        print(temp.data, end="->")
        temp = temp.next
        if temp == head:
            print(temp.data)
            break
head = None
n = int(input("Enter the number of nodes:"))
for _ in range(n):
    val = int(input("Enter the value:"))
    head = insert_begin(head, val)
display(head)'''

# circular linked list insert at end
class node:
    def __init__(self,data):
        self.data = data
        self.next = None
def insert_end(head, data):
    new = node(data)
    if head is None:
        new.next = new
        return new
    temp = head
    while temp.next != head:
        temp = temp.next
    temp.next = new
    new.next = head
    return head
def display(head):
    if head is None:
        return
    temp = head
    while True:
        print(temp.data, end="->")
        temp = temp.next
        if temp == head:
            print(temp.data)
            break
head = None
n = int(input("Enter the number of nodes:"))
for _ in range(n):
    val = int(input("Enter the value:"))
    head = insert_end(head, val)
display(head)