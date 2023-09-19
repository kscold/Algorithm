class Node:
    def __init__(self, val):
        self.val = val
        self.leftChild = None
        self.rightChild = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def setRoot(self, val): # 루트 노드를 설정
        self.root = Node(val)

    # 노드 value가 존재하는지 탐색
    def find(self, val):
        if (self.findNode(self.root, val) is False):
            return False
        else:
            return True

    def findNode(self, currentNode, val):
        if (currentNode is None):
            return False
        elif (val == currentNode.val):
            return currentNode
        elif (val < currentNode.val):
            return self.findNode(currentNode.leftChild, val)
        else:
            return self.findNode(currentNode.rightChild, val)

    def insert(self, val):
        if (self.root is None):
            self.setRoot(val)
        else:
            self.insertNode(self.root, val)

    def insertNode(self, currentNode, val):
        if (val <= currentNode.val):
            if (currentNode.leftChild):
                self.insertNode(currentNode.leftChild, val)
            else:
                currentNode.leftChild = Node(val)
        elif (val > currentNode.val):
            if (currentNode.rightChild):
                self.insertNode(currentNode.rightChild, val)
            else:
                currentNode.rightChild = Node(val)

# BinarySearchTree 클래스의 인스턴스 생성
bst = BinarySearchTree()

# 루트 노드 설정
bst.setRoot(50)

# 다른 값들을 삽입
bst.root.leftChild = Node(30)
bst.root.rightChild = Node(70)
bst.root.leftChild.leftChild = Node(20)
bst.root.leftChild.rightChild = Node(40)
bst.root.rightChild.leftChild = Node(60)
bst.root.rightChild.rightChild = Node(80)

# 원하는 노드를 삽입
bst.insert(120)

# 값 찾기
value_to_find = 120
if bst.find(value_to_find):
    print(f"{value_to_find}를 찾았습니다.")
else:
    print(f"{value_to_find}를 찾지 못했습니다.")

