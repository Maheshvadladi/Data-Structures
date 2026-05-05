# tree implementation

'''class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
root = node(10)
root.left = node(5)
root.right = node(15)
root.left.left = node(3)
root.left.right = node(7)
root.left.left.left = node(1)
root.left.left.right = node(4)'''

# inorder traversal
'''class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def tree(arr, i, n):
    if i < n:
        nd = node(arr[i])
        nd.left = tree(arr, 2*i+1, n)
        nd.right = tree(arr, 2*i+2, n)
        return nd
    return None
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)
n = int(input("Enter the number of nodes: "))
arr = []
print("\n enter node value: ")
for i in range(n):
    val = int(input("Enter value: "))
    arr.append(val)
root = tree(arr, 0, n)
print("Tree data: ", inorder(root))'''

# preorder traversel
'''class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def tree(arr, i, n):
    if i < n:
        nd = node(arr[i])
        nd.left = tree(arr, 2*i+1, n)
        nd.right = tree(arr, 2*i+2, n)
        return nd
    return None
def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)
n = int(input("Enter the number of nodes: "))
arr = []
print("\n enter node value: ")
for i in range(n):
    val = int(input("Enter value: "))
    arr.append(val)
root = tree(arr, 0, n)
print("Tree data: ", preorder(root))'''

# postorder traversel
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def tree(arr, i, n):
    if i < n:
        nd = node(arr[i])
        nd.left = tree(arr, 2*i+1, n)
        nd.right = tree(arr, 2*i+2, n)
        return nd
    return None
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")
n = int(input("Enter the number of nodes: "))
arr = []
print("\n enter node value: ")
for i in range(n):
    val = int(input("Enter value: "))
    arr.append(val)
root = tree(arr, 0, n)
print("Tree data: ", postorder(root))