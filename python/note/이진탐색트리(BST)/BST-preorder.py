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

# 이진 트리 생성 및 순회 실행 예시
bst = BinarySearchTree()
bst.setRoot(1)
bst.root.leftChild = Node(3)
bst.root.rightChild = Node(2)
bst.root.leftChild.leftChild = Node(4)
bst.root.leftChild.rightChild = Node(5)

print("Preorder: ", end='')
bst.preorder()  # 출력: Preorder: 1 3 4 5 2

print("")

