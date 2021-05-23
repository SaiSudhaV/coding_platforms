class Node:
  
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def insert(self, root, i):
        if not root: 
            return Node(i) 
        elif root.data < i:
            root.right = self.insert(root.right, i)
        else:
            root.left = self.insert(root.left, i) 
        return root


    def create(self, ar, n):
        root = Node(ar[0])
        for i in range(1, n):
            root = self.insert(root, ar[i])
        return root

def bottom_up_level_order(root):
    tem = [i for i in range(1, heightOfTree(root) + 1)]
    for i in reversed(tem):
        level_wise_elements(root, i)
        print()

def level_wise_elements(root, n):
    if root is None:
        return 
    if n == 1 :
        print(root.data, end = " ")
    elif n > 1:
        level_wise_elements(root.left, n - 1)
        level_wise_elements(root.right, n - 1)

def heightOfTree(root):
    if not root:
        return 0
    return 1 + max(heightOfTree(root.right), heightOfTree(root.left))
        
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        ar = list(map(int, input().split()))
        root = BST().create(ar, n)
        bottom_up_level_order(root)
        print()