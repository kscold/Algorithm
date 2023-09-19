class Node:
    def __init__(self, val):
        self.val = val
        self.leftChild = None
        self.rightChild = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def setRoot(self, val):
        self.root = Node(val)

    # 전위 순회
    def preorder(self):
        def _preorder(node):
            if node:
                print(node.val, end=' ')
                _preorder(node.leftChild)
                _preorder(node.rightChild)

        _preorder(self.root)

    # 중위 순회
    def inorder(self):
        def _inorder(node):
            if node:
                _inorder(node.leftChild)
                print(node.val, end=' ')
                _inorder(node.rightChild)

        _inorder(self.root)

    # 후위 순회
    def postorder(self):
        def _postorder(node):
            if node:
                _postorder(node.leftChild)
                _postorder(node.rightChild)
                print(node.val, end=' ')

        _postorder(self.root)

# 이진 트리 생성 및 순회 실행 예시
bst = BinarySearchTree()
bst.setRoot(1)
bst.root.leftChild = Node(3)
bst.root.rightChild = Node(2)
bst.root.leftChild.leftChild = Node(4)
bst.root.leftChild.rightChild = Node(5)

print("Inorder: ", end='')
bst.inorder()
