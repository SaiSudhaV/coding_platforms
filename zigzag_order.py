class Node(object):
    def __init__(self, x):
        self.data = x
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

def zigzagLevelOrder(root):
    temp,ptr, flag = [], [], True
    if not root:
        return
    temp.append(root)
    while len(temp) > 0:
        x = temp.pop(-1)
        print(x.data, end=" ")
        if flag:
            if x.right:
                ptr.append(x.right)
            if x.left:
                ptr.append(x.left)
        else:
            if x.left:
                ptr.append(x.left)
            if x.right:
                ptr.append(x.right)
        if not len(temp):
            flag = not flag
            temp, ptr = ptr, temp

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        ar = list(map(int, input().split()))
        root = BST().create(ar, n)
        zigzagLevelOrder(root)
        print()