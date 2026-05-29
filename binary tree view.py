'''#Left view of a tree 
from collections import deque
class treenode:
    def _init_(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def leftview(root):
    if root is None:
        return[]
    result = []
    queue=deque([root])
    while queue:
        levelsize=len(queue)
        result.append(queue[0].val)
        for _ in range(levelsize):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return result
if _name=='main_':
    root=treenode(1)
    root.left=treenode(2)
    root.right=treenode(3)
    root.left.left=treenode(4)
    root.left.right=treenode(5)
    root.right.right=treenode(6)
    root.left.right.left=treenode(7)
    root.right.right.right=treenode(8)
    print("left View :",leftview(root))'''



#right view of a tree 
'''from collections import deque
class treenode:
    def _init_(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def leftview(root):
    if root is None:
        return[]
    result = []
    queue=deque([root])
    while queue:
        levelsize=len(queue)
        result.append(queue[-1].val)
        for _ in range(levelsize):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return result
if __name__=='main_':
    root=treenode(1)
    root.left=treenode(2)
    root.right=treenode(3)
    root.left.left=treenode(4)
    root.left.right=treenode(5)
    root.right.right=treenode(6)
    root.left.right.left=treenode(7)
    root.right.right.right=treenode(8)
    print("left View :",leftview(root))'''

#vertical order traversal of a tree 
'''from collections import deque, defaultdict 
class treenode:
    def _init_(self, val= 0 , left= None, right=None):
        self.val= val
        self.left = left
        self.right= right 
def vot(root):
    if not root:
        return []
    col_map= defaultdict(list)
    queue= deque([(root,0)])
    while queue:
        node, hd= queue.popleft()
        col_map[hd].append(node.val)
        if node.left:
            queue.append((node.left, hd-1))
        if node.right:
            queue.append((node.right, hd+1))
    result= []
    for hd in sorted(col_map.keys()):
        result.append(col_map[hd])
    return result
if __name__=='main_':
    root= treenode(1)
    root.left= treenode(2)
    root.right= treenode(3)
    root.left.left= treenode(4)
    root.left.right= treenode(5)
    root.right.right= treenode(6)
    root.left.right.left= treenode(7)
    root.right.right.right= treenode(8)
    result= vot(root)
    print("Vertical order traversal:")
    for c in result:
        print(c)'''

# top view of a tree
'''from collections import deque
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def topView(root):
    q = deque()
    q.append((root, 0))
    d = {}
    while q:
        node, hd = q.popleft()
        if hd not in  d:
            d[hd] = node.data
        if node.left:
            q.append((node.left, hd-1))
        if node.right:
            q.append((node.right, hd+1))

    for i in sorted(d):
        print(d[i], end=" ")
root = node(1)
root.left = node(2)
root.right = node(3)
root.left.right = node(4)
root.right.left = node(5)
root.right.right = node(6)
print("Top View:")
topView(root)'''

# bottom view of a tree
'''from collections import deque
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def BottomView(root):
    q = deque()
    q.append((root, 0))
    d = {}
    while q:
        node, hd = q.popleft()
        d[hd] = node.data
        if node.left:
            q.append((node.left, hd-1))
        if node.right:
            q.append((node.right, hd+1))

    for i in sorted(d):
        print(d[i], end=" ")
root = node(1)
root.left = node(2)
root.right = node(3)
root.left.right = node(4)
root.right.left = node(5)
root.right.right = node(6)
print("Top View:")
BottomView(root)'''

# Boundary view/ Traversal of a tree
'''from collections import deque
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def View(root):
    q = deque()
    q.append((root, 0))
    top = {}
    bottom = {}
    while q:
        node, hd = q.popleft()
        if hd not in top:
            top[hd] = node.data
        bottom[hd] = node.data
        if node.left:
            q.append((node.left, hd-1))
        if node.right:
            q.append((node.right, hd+1))
    result = []
    for i in sorted(top):
        result.append(top[i])
    for i in sorted(bottom):
        if bottom[i] not in result:
            result.append(bottom[i])
    print(*result)
root = node(1)
root.left = node(2)
root.right = node(3)
root.left.right = node(4)
root.right.left = node(5)
root.right.right = node(6)
print("boundary View:")
View(root)'''