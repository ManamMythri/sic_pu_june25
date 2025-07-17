class TreeNode:
    def __init__(self, x):
        self.x = x
        self.L = None
        self.R = None

def insert(root, val):
    if root is None:
        return TreeNode(val)
    if val < root.x:
        root.L = insert(root.L, val)
    else:
        root.R = insert(root.R, val)
    return root

def height(root):
    if root is None:
        return -1 
    return 1 + max(height(root.L), height(root.R))


n = int(input())  
values = list(map(int, input().split()))

# Build the BST
root = None
for val in values:
    root = insert(root, val)

print(height(root))