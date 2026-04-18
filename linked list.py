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

class node:
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
print("Tail")