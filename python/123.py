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
            self.preorder(tmp.get(node.left))  # node.left가 딕셔너리에 key에 존재하지 않으면 None을 반환 node = node.left로 치환을 하면 편함
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
    tmp[root] = Node(root, left, right)  # 'A' : Node('A', 'B', 'C') 형식으로 key와 객체 value로 들어가게 됨

# tmp = {
#     'A': Node('A', 'B', 'C'),
#     'B': Node('B', 'D', '.'),
#     'C': Node('C', 'E', 'F'),
#     'D': Node('D', '.', '.'),
#     'E': Node('E', '.', '.'),
#     'F': Node('F', '.', 'G'),
#     'G': Node('G', '.', '.')
# }

# 루트 노드를 찾아서 설정
root_nodes = set(tmp.keys())  # tmp 딕셔너리의 key값들만 추출 set 집합으로 만듬, 모든 노드의 루트 값을 저장
child_nodes = set()  # set 집합의 인스턴스를 생성, 자식 노드의 값을 저장
for key in tmp:
    if tmp[key].left != '.':  # 딕셔너리의 value가 left가 .일 때
        child_nodes.add(tmp[key].left)  # tmp[key] 해당 키에 대응하는 값(value)을 나타낸다.
    if tmp[key].right != '.':
        child_nodes.add(tmp[key].right)

root_node = (root_nodes - child_nodes - set(['.'])).pop()  # 처음 root 노드만 남기고 삭제 즉 루트 노드를 구함
tree.root = tmp[root_node]  # tmp[roo_node]를 가리키므로 처음 루트 노드의 값을 저장

tree.preorder(tree.root)
print("")
tree.inorder(tree.root)
print("")
tree.postorder(tree.root)
