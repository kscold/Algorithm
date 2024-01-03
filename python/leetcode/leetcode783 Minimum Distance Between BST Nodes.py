#
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#
# class BST:
#     def __init__(self, root):
#         self.root = root # 루트 노드
#
#     def insert_node(self, value):
#         self.base_node = self.root
#
#         while True:
#             if self.base_node.value > value:
#                 if self.base_node.left != None :
#                     self.base_node = self.base_node.left
#                 else:
#                     self.base_node.left = Node(value)
#                     break
#             elif self.base_node.value < value:
#                 if self.base_node.right != None:
#                     self.base_node = self.base_node.right
#                 else:
#                     self.base_node.right = Node(value)
#                     break
#             else:
#                 break
#
# def inorder(node, result):
#     if node is not None:
#         inorder(node.left, result)
#         result.append(node.value)
#         inorder(node.right, result)
#
#
#
# A = input().split()
#
# head = Node(int(A[0]))
# bt = BST(head)
#
# for val in A[1:]:
#     if val != 'null':
#         bt.insert_node(int(val))
#
# # 중위 순회를 통해 모든 노드 값을 저장
# values = []
# inorder(head, values)
#
# # 최소값 계산
# min_diff = float('inf')
# for i in range(1, len(values)):
#     diff = values[i] - values[i - 1]
#     min_diff = min(min_diff, diff)
#
# print(min_diff)


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    prev = -100000
    result = 100000

    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root.left:
            self.minDiffInBST(root.left)

        self.result = min(self.result, root.val - self.prev)
        self.prev = root.val

        if root.right:
            self.minDiffInBST(root.right)

        return self.result

# 주어진 리스트로부터 이진 트리 생성
def createTree(nums):
    if not nums:
        return None

    root = TreeNode(nums[0])
    queue = [root]
    i = 1

    while queue and i < len(nums):
        node = queue.pop(0)

        left_val = nums[i]
        i += 1
        right_val = nums[i]
        i += 1

        if left_val is not None:
            node.left = TreeNode(left_val)
            queue.append(node.left)

        if right_val is not None:
            node.right = TreeNode(right_val)
            queue.append(node.right)

    return root


# 주어진 입력 리스트
# input_list = [10,5,15,3,7,None,18]

# 주어진 입력 문자열
input_str = input().split()

# "null"을 None으로 변환하고 숫자로 변환
input_list = [int(x) if x != "null" else None for x in input_str]

# 이진 트리 생성
tree_root = createTree(input_list)

# Solution 클래스의 인스턴스 생성
solution = Solution()

# 메서드 호출
result = solution.minDiffInBST(tree_root)
print(result)  # 결과 출력
