
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self, root):
        self.root = root # 루트 노드

    def insert_node(self, value):
        self.base_node = self.root

        while True:
            if self.base_node.value > value:
                if self.base_node.left != None :
                    self.base_node = self.base_node.left
                else:
                    self.base_node.left = Node(value)
                    break
            elif self.base_node.value < value:
                if self.base_node.right != None:
                    self.base_node = self.base_node.right
                else:
                    self.base_node.right = Node(value)
                    break
            else:
                break

def inorder(node, result):
    if node is not None:
        inorder(node.left, result)
        result.append(node.value)
        inorder(node.right, result)



A = input().split()

head = Node(int(A[0]))
bt = BST(head)

for val in A[1:]:
    if val != 'null':
        bt.insert_node(int(val))

# 중위 순회를 통해 모든 노드 값을 저장
values = []
inorder(head, values)

# 최소값 계산
min_diff = float('inf')
for i in range(1, len(values)):
    diff = values[i] - values[i - 1]
    min_diff = min(min_diff, diff)

print(min_diff)