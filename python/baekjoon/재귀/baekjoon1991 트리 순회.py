# 문제
# 이진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하시오.

# 예를 들어 위와 같은 이진 트리가 입력되면,

# 전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
# 중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
# 후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)
# 가 된다.

# 입력
# 첫째 줄에는 이진 트리의 노드의 개수 N(1 ≤ N ≤ 26)이 주어진다. 둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다. 노드의 이름은 A부터 차례대로 알파벳 대문자로 매겨지며, 항상 A가 루트 노드가 된다. 자식 노드가 없는 경우에는 .으로 표현한다.

# 출력
# 첫째 줄에 전위 순회, 둘째 줄에 중위 순회, 셋째 줄에 후위 순회한 결과를 출력한다. 각 줄에 N개의 알파벳을 공백 없이 출력하면 된다.

# 예제 입력 1
# 7
# A B C
# B D .
# C E F
# E . .
# F . G
# D . .
# G . .
# 예제 출력 1
# ABDCEFG
# DBAECFG
# DBEGFCA

import sys

input = sys.stdin.readline


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
            # 재귀적으로 순회
            self.preorder(datas.get(node.left))
            self.preorder(datas.get(node.right))

    def inorder(self, node):
        if node:
            self.inorder(datas.get(node.left))
            print(node.root, end='')
            self.inorder(datas.get(node.right))

    def postorder(self, node):
        if node:
            self.postorder(datas.get(node.left))
            self.postorder(datas.get(node.right))
            print(node.root, end='')


tree = BinaryTree()
datas = {}

n = int(input())

for i in range(n):
    root, left, right = map(str, input().split())
    datas[root] = Node(root, left, right)

# 루트 노드를 찾아서 설정
root_nodes = set(datas.keys())  # 데이터의 key만 뽑아서 집합으로 설정
child_nodes = set()  # 자식 노드의 정보를 저장할 집합을 선언
for key in datas:  # 딕셔너리 순회는 기본적으로 key 순회
    if datas[key].left != '.':
        child_nodes.add(datas[key].left)
    if datas[key].right != '.':
        child_nodes.add(datas[key].right)

root_node = (root_nodes - child_nodes).pop()  # 차집합하고 남은 값을 pop으로 반환하여 루트 노드를 구함
tree.root = datas[root_node]  # 루트 노드 설정

tree.preorder(tree.root)
print("")
tree.inorder(tree.root)
print("")
tree.postorder(tree.root)
