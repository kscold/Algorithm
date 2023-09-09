from collections import deque

class Node(object):
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self):
        self.root = None

    # 전위 순회

    def preorder(self):
        def _preorder(node): # node = self.root와 같음
            print(node.item, end = ' ') # 노드 root를 표시하고 개행을 무시하되 공백을 넣음 # 프린트 위치도 중요 전위 순회이므로 root를 먼저 프린트
            if node.left:
                _preorder(node.left) # node.left가 존재할 때는 _preorder를 재참조, node.left는 사실상 self.root.left와 같음
            if node.right:
                _preorder(node.right) # node.right가 존재할 때는 _preorder를 재참조
        _preorder(self.root) # node에 self.root를 대입하기 위해

    # 중위 순회 왼쪽 자식 노드, 루트 노드, 오른쪽 자식 노드 순으로 값을 확인하는 방식, 자식 노드를 확인하고 미에 자손 노드들이 있다면 자손 노드들도 동일한 방식으로 확인
    def inorder(self):
        def _inorder(node): # node = self.root
            if node.left: # self.root.left
                _inorder(node.left) # 가장 왼쪽의 노드부터 탐색
            print(node.item, end=' ') # 중위 순회이므로 중간의 node를 탐색
            if node.right:
                _inorder(node.right) # 오른쪽 노드 탐색

        _inorder(self.root) # node에 self.root를 대입

    # 후위 순회 자식 노드를 모두 탐색 후 루트 노드를 확인하는 순회 방법, 자식 노드의 자손 노드가 존재한다면 동일한 방식으로 모두 확인
    def postorder(self):
        def _postorder(node): # node = self.root
            if node.left: # self.root.left
                _postorder(node.left) # 가장 왼쪽의 노드부터 탐색
            if node.right:
                _postorder(node.right) # 오른쪽 노드 탐색
            print(node.item, end=' ')  # 후뤼 순회이므로 가장 마지막에 root 노드를 탐색

        _postorder(self.root) # node에 self.root를 대입

    # 레벨 순회 각 레벨마다 노드를 탐색하는 방법 큐를 이용해 구현할 수 있음
    def levelorder(self):
        q = deque([self.root]) # self.root 값을 deque에 넣음
        while q:
            node = q.popleft() # deque 앞(왼쪽)부터 pop함
            print(node.item, end=' ')
            if node.left:
                q.append(node.left) # 큐의 뒤(오른쪽)에 값을 추가함, 즉 큐가 점점 밀려서 왼쪽으로 옴 따라서 popleft를 하는 것임
            if node.right:
                q.append(node.right) # 큐의 뒤(오른쪽)에 값을 추가함

# 이진 트리 생성 및 순회 실행 예시
bt = BinaryTree() # BinaryTree의 인스턴스인 bt를 생성
bt.root = Node(1) # BinaryTree.root = Node(1) 즉 bt.root 인스턴스는 Node(1) -> init으로 설정
bt.root.left = Node(3) # bt.root.left = Node(2) 즉 bt.root.left 인스턴스는 Node(2) left로 설정
bt.root.right = Node(2) # # bt.root.right = Node(2) 즉 bt.root.right 인스턴스는 Node(3) right로 설정
bt.root.left.left = Node(4)
bt.root.left.right = Node(5)

# 트리 예시 그림
#      1
#    /   \
#   3     2
#  / \
# 4   5


print("Preorder: ", end='')
bt.preorder()  # 출력: Preorder: 1 3 4 5 2

print("")

print("inorder: ", end='')
bt.inorder()

print("")

print("postorder: ", end='')
bt.postorder()

print("")

print("levelorder: ", end='')
bt.levelorder()