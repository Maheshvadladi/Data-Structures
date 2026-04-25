# Detecting cycle in singly linked list

'''class node:
    def __init__(self, data):
        self.data = data
        self.next = None
head = None
def insert_end(data):
    global head
    newnode = node(data)
    if head is None:
        head = newnode
        return
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = newnode
def create_cycle(pos):
    global head
    if pos==-1:
        return
    temp = head
    cycle_node = None
    index = 0
    while temp.next:
        if index == pos:
            cycle_node = temp
        temp = temp.next
        index += 1
    if cycle_node:
        temp.next = cycle_node
def detect_cycle():
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            print("Cycle is detected")
            return
    print("No cycle is detected")
def display(limit=15):
    temp = head
    count = 0
    while temp and count< limit:
        print(temp.data, end="->")
        temp = temp.next
        count += 1
    print("None")

n = int(input("Enter the number of nodes:"))
for _ in range(n):
    val = int(input("Enter the value:"))
    insert_end(val)
print("Inserted Linkedlist:")
display()
pos = int(input("Enter the position:"))
create_cycle(pos)
detect_cycle()'''