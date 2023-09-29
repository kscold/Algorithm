# import sys
#
# N = int(sys.stdin.readline())
# tmp = {}
# class Node:
#     def __init__(self, root, left=None, right=None):
#         self.root = root
#         self.left = left
#         self.right = right
#
# class BinaryTree:
#     def __init__(self):
#         self.root = None
#
#     def preorder(self,node):
#         print(node.root,end='')
#         if node.left != '.':
#             self.preorder(tmp[node.left])
#         if node.right != '.':
#             self.preorder(tmp[node.right])
#
#     def inorder(self,node):
#         if node.left != '.':
#             self.inorder(tmp[node.left])
#         print(node.root,end='')
#         if node.right != '.':
#             self.inorder(tmp[node.right])
#
#     def postorder(self,node):
#         if node.left != '.':
#             self.postorder(tmp[node.left])
#         if node.right != '.':
#             self.postorder(tmp[node.right])
#         print(node.root,end='')
#
# for i in range(N):
#      root,left,right= map(str,sys.stdin.readline().split())
#      tmp[root]=Node(root,left,right)
#
# tree=BinaryTree()
# tree.root=tmp['A']
# tree.preorder(tree.root)
# print("")
# tree.inorder(tree.root)
# print("")
# tree.postorder(tree.root)


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

    def preorder(self, node):
        if node:
            print(node.root, end='')
            self.preorder(tmp.get(node.left)) # node.left가 딕셔너리에 존재하지 않으면 None을 반환
            self.preorder(tmp.get(node.right))

    def inorder(self, node):
        if node:
            self.inorder(tmp.get(node.left))
            print(node.root, end='')
            self.inorder(tmp.get(node.right))

    def postorder(self, node):
        if node:
            self.postorder(tmp.get(node.left))
            self.postorder(tmp.get(node.right))
            print(node.root, end='')

tree = BinaryTree()

for i in range(N):
    root, left, right = map(str, sys.stdin.readline().split())
    tmp[root] = Node(root, left, right)

# 루트 노드를 찾아서 설정
root_nodes = set(tmp.keys())
child_nodes = set()
for key in tmp:
    if tmp[key].left != '.':
        child_nodes.add(tmp[key].left)
    if tmp[key].right != '.':
        child_nodes.add(tmp[key].right)

root_node = (root_nodes - child_nodes).pop()
tree.root = tmp[root_node]

tree.preorder(tree.root)
print("")
tree.inorder(tree.root)
print("")
tree.postorder(tree.root)


