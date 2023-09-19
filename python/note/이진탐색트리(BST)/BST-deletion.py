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

    def delete(self, value):
        searched = False  # 노드가 존재하는지 여부를 나타내는 플래그
        self.current_node = self.root  # 삭제할 노드
        self.parent = None  # 삭제할 노드의 부모 노드

        # 삭제할 노드 탐색
        while self.current_node:
            if self.current_node.val == value:
                searched = True
                break
            elif value < self.current_node.val:
                self.parent = self.current_node
                self.current_node = self.current_node.leftChild  # 왼쪽 자식으로 이동
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.rightChild  # 오른쪽 자식으로 이동

        if searched == False:  # 삭제할 노드가 없다면 False 반환
            return False

        # Case 1: 삭제할 노드가 리프 노드인 경우
        if self.current_node.leftChild is None and self.current_node.rightChild is None:
            if value < self.parent.val:
                self.parent.leftChild = None  # 부모 노드의 왼쪽 링크 제거
            else:
                self.parent.rightChild = None  # 부모 노드의 오른쪽 링크 제거

        # Case 2: 삭제할 노드가 자식 노드를 한 개 가지고 있는 경우
        elif self.current_node.leftChild is None or self.current_node.rightChild is None:
            if self.current_node.leftChild is not None:  # 왼쪽 자식이 있는 경우
                if value < self.parent.val:
                    self.parent.leftChild = self.current_node.leftChild
                else:
                    self.parent.rightChild = self.current_node.leftChild
            else:  # 오른쪽 자식이 있는 경우
                if value < self.parent.val:
                    self.parent.leftChild = self.current_node.rightChild
                else:
                    self.parent.rightChild = self.current_node.rightChild

        # Case 3: 삭제할 노드가 자식 노드를 두 개 가지고 있는 경우
        else:
            # Case 3-1: 삭제할 노드가 부모 노드의 왼쪽에 있는 경우
            if value < self.parent.val:
                self.change_node = self.current_node.rightChild
                self.change_node_parent = self.current_node.rightChild

                # 가장 작은 값을 가진 노드를 찾아서 change_node에 저장
                while self.change_node.leftChild is not None:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.leftChild

                # change_node가 오른쪽 자식을 가질 경우 처리
                if self.change_node.rightChild is not None:
                    self.change_node_parent.leftChild = self.change_node.rightChild
                else:
                    self.change_node_parent.leftChild = None

                # 삭제할 노드를 대체 노드로 변경
                self.parent.leftChild = self.change_node
                self.change_node.rightChild = self.current_node.rightChild
                self.change_node.leftChild = self.current_node.leftChild

            # Case 3-2: 삭제할 노드가 부모 노드의 오른쪽에 있는 경우 (유사한 로직)
            else:
                self.change_node = self.current_node.rightChild
                self.change_node_parent = self.current_node.rightChild

                while self.change_node.leftChild is not None:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.leftChild

                if self.change_node.rightChild is not None:
                    self.change_node_parent.leftChild = self.change_node.rightChild
                else:
                    self.change_node_parent.leftChild = None

                self.parent.rightChild = self.change_node
                self.change_node.leftChild = self.current_node.leftChild
                self.change_node.rightChild = self.current_node.rightChild

        return True  # 노드 삭제 성공


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

value_to_delete = 20
bst.delete(value_to_delete)
# 값 찾기
value_to_find = 20
if bst.find(value_to_find):
    print(f"{value_to_find}를 찾았습니다.")
else:
    print(f"{value_to_find}를 찾지 못했습니다.")

