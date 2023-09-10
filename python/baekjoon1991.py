import sys

N = int(sys.stdin.readline())
tmp = {}
class Node:
    def __init__(self, root, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

    def preorder(self,node):
        print(node.root,end='')
        if node.left != '.':
            self.preorder(tmp[node.left])
        if node.right != '.':
            self.preorder(tmp[node.right])

    def inorder(self,node):
        if node.left != '.':
            self.inorder(tmp[node.left])
        print(node.root,end='')
        if node.right != '.':
            self.inorder(tmp[node.right])

    def postorder(self,node):
        if node.left != '.':
            self.postorder(tmp[node.left])
        if node.right != '.':
            self.postorder(tmp[node.right])
        print(node.root,end='')

for i in range(N):
     root,left,right= map(str,sys.stdin.readline().split())
     tmp[root]=Node(root,left,right)

tree=BinaryTree()
tree.root=tmp['A']
tree.preorder(tree.root)
print("")
tree.inorder(tree.root)
print("")
tree.postorder(tree.root)
